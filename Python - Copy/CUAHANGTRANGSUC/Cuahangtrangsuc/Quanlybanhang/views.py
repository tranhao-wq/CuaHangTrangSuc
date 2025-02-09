from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib import messages
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from .models import (
    QuayBanHang,
    NhanVien,
    HoaDon,
    SanPham,
    LoaiSanPham,
    GiaVang,
    ChiTietHoaDon,
    KhuyenMai,
    MuaLai,
    KhachHang,
)
from django.db.models import Sum, F, Q

from Quanlybanhang.forms import QuayBanHangForm, NhanVienForm
import datetime
# from home.models import UuDaiKhachHang
# Trang hiển thị danh sách các quầy bán hàng
def quaybanhangs(request):
    quaybanhangs = QuayBanHang.objects.all()
    return render(request, 'home/quaybanhang/quaybanhangs.html', {'cacquaybanhangs': quaybanhangs, 'active_menu': 'quaybanhangs'})
    # template = loader.get_template('quaybanhangs.html')
    # context = {
    #     'cacquaybanhangs': quaybanhangs,  # Truyền danh sách quầy vào context
    # }
    # return HttpResponse(template.render(context, request))

# Trang chỉnh sửa một quầy bán hàng cụ thể
def quaybanhang_edit(request, ma_quay):
    quaybanhang = get_object_or_404(QuayBanHang, ma_quay=ma_quay)

    # Lấy danh sách nhân viên từ database
    nhanviens = NhanVien.objects.all()
    # Truy vấn danh sách sản phẩm của quầy
    sanphams = quaybanhang.san_phams.all()

    # Tính tổng đơn đã bán (ví dụ)
    # bạn có thể thay thế code này bằng code query đơn hàng của bạn
    tong_don_ban = 123  # ví dụ số đơn đã bán
    form = QuayBanHangForm(instance=quaybanhang)

    if request.method == 'POST':
        form = QuayBanHangForm(request.POST, instance=quaybanhang)
        if form.is_valid():
            try:
                form.save()

                # Xử lý form thay đổi nhân viên phụ trách (nếu có)
                new_nhan_vien_ma = request.POST.get('new_nhan_vien_phu_trach')
                if new_nhan_vien_ma:
                   new_nhan_vien = get_object_or_404(NhanVien, ma_nhan_vien=new_nhan_vien_ma)
                   quaybanhang.nhan_vien_phu_trach = new_nhan_vien
                   quaybanhang.save()
                   messages.success(request, 'Đã thay đổi nhân viên phụ trách thành công!')
                else:
                   messages.error(request, 'Lỗi không tìm thấy nhân viên!')
            except Exception as e:
                print(f"Lỗi khi lưu thông tin quầy: {e}")  # In ra console
                return JsonResponse({'success': False, 'error': str(e)})


            # Xử lý form tạo hóa đơn bán hàng (nếu có)
            ma_hoa_don = request.POST.get('ma_hoa_don')
            ngay_lap = request.POST.get('ngay_lap')
            tong_tien = request.POST.get('tong_tien')
            ma_khach_hang = request.POST.get('ma_khach_hang')
            if ma_hoa_don and ngay_lap and tong_tien and ma_khach_hang:
                try:
                    HoaDon.objects.create(
                        ma_hoa_don=ma_hoa_don,
                        ngay_lap=ngay_lap,
                        tong_tien=tong_tien,
                        ma_khach_hang=ma_khach_hang,
                    )
                    messages.success(request, 'Đã tạo hóa đơn bán hàng thành công!')
                except Exception as e:
                    messages.error(request, f'Lỗi khi tạo hóa đơn bán hàng: {e}')

             # Xử lý form in hóa đơn bán hàng (nếu có)
            ma_hoa_don_in = request.POST.get('ma_hoa_don_in')
            if ma_hoa_don_in:
                 try:
                      hoa_don = get_object_or_404(HoaDon, ma_hoa_don=ma_hoa_don_in)
                     # Tạo file PDF
                      response = HttpResponse(content_type='application/pdf')
                      response['Content-Disposition'] = f'attachment; filename="hoa_don_{ma_hoa_don_in}.pdf"'
                      p = Canvas(response, pagesize=letter)
                      p.drawString(1 * inch, 10.5 * inch, f'Mã hóa đơn: {hoa_don.ma_hoa_don}')
                      p.drawString(1 * inch, 10 * inch, f'Ngày lập: {hoa_don.ngay_lap}')
                      p.drawString(1 * inch, 9.5 * inch, f'Tổng tiền: {hoa_don.tong_tien}')
                      p.drawString(1 * inch, 9 * inch, f'Mã khách hàng: {hoa_don.ma_khach_hang}')
                      p.save()
                      return response
                 except Exception as e:
                      messages.error(request, f'Lỗi khi in hóa đơn bán hàng: {e}')

            # Xử lý form in phiếu bảo hành
            ma_san_pham_bao_hanh = request.POST.get('ma_san_pham_bao_hanh')
            ma_khach_hang_bao_hanh = request.POST.get('ma_khach_hang_bao_hanh')
            if ma_san_pham_bao_hanh and ma_khach_hang_bao_hanh:
                 try:
                    # Tạo file PDF phiếu bảo hành
                    response = HttpResponse(content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename="phieu_bao_hanh_{ma_san_pham_bao_hanh}.pdf"'
                    p = Canvas(response, pagesize=letter)
                    p.drawString(1 * inch, 10.5 * inch, f'Mã sản phẩm: {ma_san_pham_bao_hanh}')
                    p.drawString(1 * inch, 10 * inch, f'Mã khách hàng: {ma_khach_hang_bao_hanh}')
                    p.drawString(1 * inch, 9.5 * inch, 'Thời gian bảo hành: 1 năm')
                    p.save()
                    return response
                 except Exception as e:
                    messages.error(request, f'Lỗi khi in phiếu bảo hành: {e}')

            messages.success(request, 'Đã lưu thông tin quầy thành công!')
            return redirect('quaybanhangs')
        else:
             messages.error(request, 'Lỗi khi lưu thông tin quầy')

    context = {
        'quaybanhang': quaybanhang,
        'nhanviens': nhanviens,
        'sanphams': sanphams,
        'tong_don_ban': tong_don_ban,
        'form': form,
         'active_menu': 'quaybanhangs'
      }
    return render(request, 'home/quaybanhang/quaybanhang-edit.html', context)


def quaybanhang_delete(request, ma_quay):
    quaybanhang = get_object_or_404(QuayBanHang, ma_quay=ma_quay)
    quaybanhang.delete()
    messages.success(request, "Quầy bán hàng đã được xóa thành công!")  # Thông báo thành công
    return redirect('quaybanhangs')  # Điều hướng đến danh sách quầy bán hàng


def quaybanhang_new(request):
    if request.method == 'POST':
        form = QuayBanHangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quaybanhangs')  # Chuyển hướng đến danh sách quầy
    else:
        form = QuayBanHangForm()

    return render(request, 'quaybanhang-new.html', {'form': form, 'active_menu': 'quaybanhangs'})


def nhanviens(request):
    nhanviens = NhanVien.objects.all()
    if request.method == 'POST':
         if 'add_employee' in request.POST:
            form = NhanVienForm(request.POST)
            if form.is_valid():
                try:
                  form.save()
                  messages.success(request, "Nhân viên đã được thêm thành công!")
                  return redirect('nhanviens')
                except Exception as e:
                    messages.error(request, f'Lỗi khi tạo nhân viên: {e}')
            else:
                messages.error(request, 'Lỗi khi thêm nhân viên')
         elif 'edit_employee' in request.POST:
            ma_nhan_vien = request.POST.get('ma_nhan_vien')
            if ma_nhan_vien:
               nhanvien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
               form = NhanVienForm(request.POST, instance=nhanvien)
               if form.is_valid():
                     try:
                         form.save()
                         messages.success(request, "Thông tin nhân viên đã được chỉnh sửa thành công!")
                         return redirect('nhanviens')
                     except Exception as e:
                        messages.error(request, f"Lỗi khi chỉnh sửa nhân viên {e}")
               else:
                   messages.error(request, "Lỗi khi chỉnh sửa thông tin nhân viên")
         else:
           ma_nhan_vien = request.POST.get('ma_nhan_vien')
           if ma_nhan_vien:
               nhanvien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
               nhanvien.delete()
               messages.success(request, "Nhân viên đã được xóa thành công!")
               return redirect('nhanviens')

    return render(request, 'home/nhanvien/nhanviens.html', {'nhanviens': nhanviens, 'active_menu': 'nhanviens'})

def nhanvien_edit(request, ma_nhan_vien):
    nhanvien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
    if request.method == 'POST':
        form = NhanVienForm(request.POST, instance=nhanvien)
        if form.is_valid():
            form.save()
            return redirect('nhanviens')
    else:
        form = NhanVienForm(instance=nhanvien)
    
    return render(request, 'nhanvien-edit.html', {'form': form, 'nhanvien': nhanvien, 'active_menu': 'nhanviens'})

def nhanvien_delete(request, ma_nhan_vien):
    nhanvien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
    nhanvien.delete()
    return redirect('nhanviens')  # Quay lại danh sách nhân viên sau khi xóa

def nhanvien_new(request):
    if request.method == 'POST':
        form = NhanVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nhanviens')  # Điều hướng đến danh sách nhân viên
    else:
        form = NhanVienForm()
    
    return render(request, 'nhanvien-new.html', {'form': form, 'active_menu': 'nhanviens'})

def nhanvien_delete(request, ma_nhan_vien):
    nhanvien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
    nhanvien.delete()
    return redirect('nhanviens')  # Quay lại danh sách nhân viên sau khi xóa

def nhanvien_new(request):
    if request.method == 'POST':
        form = NhanVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nhanviens')  # Điều hướng đến danh sách nhân viên
    else:
        form = NhanVienForm()
    
    return render(request, 'nhanvien-new.html', {'form': form, 'active_menu': 'nhanviens'})


# def khuyenmai(request):
#     return render(request, 'home/khuyenmais.html') # nhớ tạo template

def san_pham_list(request):
    # Lấy tất cả các sản phẩm từ database
    san_phams = SanPham.objects.all()
    
    # Render template với context là danh sách sản phẩm và active menu
    return render(request, "home/sanpham/sanpham.html", {"san_phams": san_phams, 'active_menu': 'quanlysanpham'})
    
def khuyen_mai_list(request):
     khuyen_mais = KhuyenMai.objects.all()
     return render(request, 'khuyen_mai_list.html', {'khuyen_mais': khuyen_mais, 'active_menu': 'quanlykhuyenmai'})

def gia_vang_list(request):
    gia_vangs = GiaVang.objects.all()
    return render(request, "gia_vang_list.html", {"gia_vangs": gia_vangs, 'active_menu': 'quanlygiavang'})

def hoa_don_list(request):
    hoa_dons = HoaDon.objects.all()
    return render(request, "hoa_don_list.html", {"hoa_dons": hoa_dons, 'active_menu': 'quanlyhoadon'})

def chi_tiet_hoa_don_list(request):
    chi_tiet_hoa_dons = ChiTietHoaDon.objects.all()
    return render(request, "chi_tiet_hoa_don_list.html", {"chi_tiet_hoa_dons": chi_tiet_hoa_dons, 'active_menu': 'quanlychitiethoadon'})

def doanhthu(request):
    # Calculate total revenue for this month
    now = datetime.now()
    start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    tong_doanh_thu_thang_nay = HoaDon.objects.filter(ngay_lap__gte=start_of_month).aggregate(Sum('tong_tien'))['tong_tien__sum'] or 0

    # Calculate total revenue for this year
    start_of_year = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    tong_doanh_thu_nam_nay = HoaDon.objects.filter(ngay_lap__gte=start_of_year).aggregate(Sum('tong_tien'))['tong_tien__sum'] or 0


    # Calculate revenue by counter
    doanh_thu_theo_quay = []
    for quay in QuayBanHang.objects.all():
         doanh_thu_thang_nay_quay =  ChiTietHoaDon.objects.filter(
               ma_hoa_don__ngay_lap__gte=start_of_month,
               ma_san_pham__quays=quay
            ).aggregate(total=Sum(F('so_luong') * F('don_gia')))['total'] or 0
         doanh_thu_nam_nay_quay = ChiTietHoaDon.objects.filter(
               ma_hoa_don__ngay_lap__gte=start_of_year,
               ma_san_pham__quays=quay
           ).aggregate(total=Sum(F('so_luong') * F('don_gia')))['total'] or 0
         doanh_thu_theo_quay.append({
                'ten_quay': quay.ten_quay,
                'doanh_thu_thang_nay': doanh_thu_thang_nay_quay,
                'doanh_thu_nam_nay': doanh_thu_nam_nay_quay,
         })

    # Calculate revenue by employee
    doanh_thu_theo_nhan_vien = []
    for nhanvien in NhanVien.objects.all():
          doanh_thu_thang_nay_nv = ChiTietHoaDon.objects.filter(
                ma_hoa_don__ngay_lap__gte=start_of_month,
              ma_san_pham__quays__nhan_vien_phu_trach=nhanvien
            ).aggregate(total=Sum(F('so_luong') * F('don_gia')))['total'] or 0
          doanh_thu_nam_nay_nv =  ChiTietHoaDon.objects.filter(
                ma_hoa_don__ngay_lap__gte=start_of_year,
               ma_san_pham__quays__nhan_vien_phu_trach=nhanvien
            ).aggregate(total=Sum(F('so_luong') * F('don_gia')))['total'] or 0
          doanh_thu_theo_nhan_vien.append({
                 'ho_ten': nhanvien.ho_ten,
                'doanh_thu_thang_nay': doanh_thu_thang_nay_nv,
                 'doanh_thu_nam_nay': doanh_thu_nam_nay_nv,
            })
   

    context = {
        'active_menu': 'doanhthu',
         'tong_doanh_thu_thang_nay': tong_doanh_thu_thang_nay,
        'tong_doanh_thu_nam_nay': tong_doanh_thu_nam_nay,
        'doanh_thu_theo_quay': doanh_thu_theo_quay,
        'doanh_thu_theo_nhan_vien': doanh_thu_theo_nhan_vien,
    }
    return render(request, 'doanhthu.html', context)

def mualai(request):
    now = datetime.now()
    start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    current_gia_vang = GiaVang.objects.order_by('-thoi_gian').first()  # Get current gold price
    tong_tien_mua_lai_thang_nay = MuaLai.objects.filter(ngay_mua_lai__gte=start_of_month).aggregate(Sum('gia_mua_lai'))['gia_mua_lai__sum'] or 0
    tong_giao_dich_mua_lai_thang_nay = MuaLai.objects.filter(ngay_mua_lai__gte=start_of_month).count()

    if request.method == 'POST':
         if 'create_buyback' in request.POST:
           try:
                ma_hoa_don = request.POST.get('ma_hoa_don')
                ma_san_pham = request.POST.get('ma_san_pham')
                gia_mua_lai = request.POST.get('gia_mua_lai')
                ghi_chu = request.POST.get('ghi_chu')


                if ma_hoa_don and ma_san_pham and gia_mua_lai:
                     hoa_don = get_object_or_404(HoaDon, ma_hoa_don=ma_hoa_don)
                     san_pham = get_object_or_404(SanPham, ma_san_pham=ma_san_pham)
                     MuaLai.objects.create(
                           ma_hoa_don = hoa_don,
                         san_pham = san_pham,
                           gia_mua_lai = gia_mua_lai,
                            ghi_chu = ghi_chu,
                        ngay_mua_lai = now

                         )
                     messages.success(request, f"Đã thêm giao dịch mua lại cho sản phẩm {ma_san_pham}")
                     return redirect('mualai')
                else:
                    messages.error(request, f"Vui lòng điền đầy đủ thông tin!")

           except Exception as e:
               messages.error(request, f"Lỗi khi tạo giao dịch mua lại: {e}")
    context = {
        'active_menu': 'mualai',
         'current_gia_vang': current_gia_vang,
         'tong_tien_mua_lai_thang_nay': tong_tien_mua_lai_thang_nay,
         'tong_giao_dich_mua_lai_thang_nay': tong_giao_dich_mua_lai_thang_nay,
    }
    return render(request, 'mualai.html', context)