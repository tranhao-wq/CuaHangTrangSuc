from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import HoaDon, QuayBanHang, NhanVien, ChiTietHoaDon
from Quanlybanhang.models import UuDaiKhachHang, KhachHang, KhuyenMai, SanPham,TichDiem  # Import from Quanlybanhang
from .forms import KhuyenMaiForm, UuDaiKhachHangForm # Import from home
from home.models import KhuyenMai
from django.http import Http404

from django.db.models import Sum, F, Q
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from Quanlybanhang.models import HoaDon
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from Quanlybanhang.models import QuayBanHang
from Quanlybanhang.forms import QuayBanHangForm
from Quanlybanhang.models import NhanVien  # Import model NhanVien
from Quanlybanhang.forms import NhanVienForm  # Import form NhanVienForm
from Quanlybanhang.forms import SanPham  # Import form NhanVienForm
from Quanlybanhang.forms import SanPhamForm  # Import form NhanVienForm
import datetime
from .forms import KhuyenMaiForm, UuDaiKhachHangForm # Import from home

from reportlab.pdfgen.canvas import Canvas

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

# Trang hiển thị danh sách các quầy bán hàng
def quaybanhangs(request):
    quaybanhangs = QuayBanHang.objects.all()
    template = loader.get_template('home/quaybanhang/quaybanhangs.html')
    context = {
        'active_menu': 'quaybanhangs',
        'cacquaybanhangs': quaybanhangs,  # Truyền danh sách quầy vào context
    }
    return HttpResponse(template.render(context, request))

def sanpham(request):
    # Lấy tất cả các sản phẩm
    san_phams = SanPham.objects.all()
    
    # Sử dụng loader để lấy template
    template = loader.get_template('home/sanpham/sanpham.html')
    
    # Truyền danh sách sản phẩm và active menu vào context
    context = {
        'active_menu': 'sanpham',  # Để làm mục này active trong menu
        'san_phams': san_phams,    # Truyền danh sách sản phẩm vào context
    }
    
    # Render template với context
    return HttpResponse(template.render(context, request))


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
      }
    return render(request, 'home/quaybanhang/quaybanhang-edit.html', context)


def khuyenmai(request):
    khuyen_mai = KhuyenMai.objects.all()
    uudais = UuDaiKhachHang.objects.all()
    sanphams = SanPham.objects.all() # Get list of san phams
    if request.method == 'POST':
        if 'add_company_promotion' in request.POST:
              try:
                ma_khuyen_mai = request.POST.get('ma_khuyen_mai')
                ma_san_pham = request.POST.get('ma_san_pham')
                phan_tram_chiet_khau = request.POST.get('phan_tram_chiet_khau')
                ngay_bat_dau = request.POST.get('ngay_bat_dau')
                ngay_ket_thuc = request.POST.get('ngay_ket_thuc')


                if ma_khuyen_mai and ma_san_pham and phan_tram_chiet_khau and ngay_bat_dau and ngay_ket_thuc:
                    sanpham = get_object_or_404(SanPham, ma_san_pham=ma_san_pham)
                    KhuyenMai.objects.create(
                        ma_khuyen_mai = ma_khuyen_mai,
                        ma_san_pham = sanpham,
                        phan_tram_chiet_khau = phan_tram_chiet_khau,
                        ngay_bat_dau = ngay_bat_dau,
                        ngay_ket_thuc = ngay_ket_thuc
                       )
                    messages.success(request, "Khuyến mãi công ty đã được thêm thành công!")
                    return redirect('khuyenmai')
                else:
                  messages.error(request, 'Vui lòng điền đầy đủ thông tin!')
              except Exception as e:
                messages.error(request, f'Lỗi khi tạo khuyến mãi: {e}')
        elif 'add_customer_discount' in request.POST:
              try:
                   ma_khach_hang = request.POST.get('ma_khach_hang')
                   phan_tram_chiet_khau = request.POST.get('phan_tram_chiet_khau')
                   if ma_khach_hang and phan_tram_chiet_khau:
                      UuDaiKhachHang.objects.create(
                          ma_khach_hang = ma_khach_hang,
                          phan_tram_chiet_khau = phan_tram_chiet_khau
                      )
                      messages.success(request, 'Đã thêm ưu đãi khách hàng thành công!')
                      return redirect('khuyenmai')
                   else:
                     messages.error(request, "Vui lòng điền đầy đủ thông tin!")
              except Exception as e:
                   messages.error(request, f"Lỗi khi thêm ưu đãi khách hàng: {e}")
        
    context = {
        'active_menu': 'khuyenmai',
        'khuyenmais': khuyen_mai,
        'uudais': uudais,
        'sanphams': sanphams,
    }
    return render(request, 'home/khuyenmai/khuyenmai.html', context)


def duyet_uudai(request, id):
    if request.method == "POST":
        uudai = get_object_or_404(UuDaiKhachHang, pk=id)
        uudai.duoc_duyet = True
        uudai.save()
        return JsonResponse({"success": True, "message": f"Đã duyệt ưu đãi cho khách hàng {uudai.ma_khach_hang}!", "uudai_id": id})
    
    return JsonResponse({"success": False, "message": "Yêu cầu không hợp lệ!"})

def delete_uudai(request, id):
    if request.method == 'POST':  # Chỉ xử lý khi yêu cầu là POST
        try:
            uutai = get_object_or_404(UuDaiKhachHang, pk=id)
            uutai.delete()
            return JsonResponse({'success': True, 'message': f"Đã xóa ưu đãi thành công!"})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"Đã xảy ra lỗi khi xóa ưu đãi. Lỗi: {str(e)}"})
    return JsonResponse({'success': False, 'message': 'Yêu cầu không hợp lệ.'})


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

    return render(request, 'home/quaybanhang/quaybanhang-new.html', {'form': form})


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
         else: # Handle delete
            ma_nhan_vien = request.POST.get('ma_nhan_vien')
            if ma_nhan_vien:
                  nhanvien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
                  nhanvien.delete()
                  messages.success(request, "Nhân viên đã được xóa thành công!")
                  return redirect('nhanviens')
    return render(request, 'home/nhanvien/nhanviens.html', {'nhanviens': nhanviens, 'active_menu': 'nhanviens'})

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
    
    return render(request, 'home/nhanvien/nhanvien-new.html', {'form': form})



def quet_barcode(request):
 return render(request, 'home/quetbarcode.html')

def quet_barcode(request):
   if request.method == 'POST':
      barcode = request.POST.get('barcode_result')
      try:
          san_pham = get_object_or_404(SanPham, ma_san_pham=barcode)
          messages.success(request, f'Đã tìm thấy sản phẩm: {san_pham.ten_san_pham} ({barcode})')
          return render(request, 'home/quetbarcode.html')
      except Exception as e:
        messages.error(request, f'Lỗi không tìm thấy sản phẩm {e}')
   return render(request, 'home/quetbarcode.html')

def process_barcode(request):
    barcode = request.GET.get('barcode', '')
    # Xử lý barcode, ví dụ tìm sản phẩm trong database
    try:
        product = SanPham.objects.get(ma_san_pham=barcode)
        return JsonResponse({"message": f"Sản phẩm: {product.ten_san_pham}"})
    except SanPham.DoesNotExist:
        return JsonResponse({"message": "Không tìm thấy sản phẩm"}, status=404)
    
def handle_barcode(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')  # Lấy mã barcode từ POST request
        if barcode:
            try:
                san_pham = SanPham.objects.get(ma_san_pham=barcode)
                message = f"Đã tìm thấy sản phẩm: {san_pham.ten_san_pham} ({barcode})"
                return JsonResponse({"success": True, "message": message})
            except SanPham.DoesNotExist:
                return JsonResponse({"success": False, "message": "Không tìm thấy sản phẩm!"})
        else:
            return JsonResponse({"success": False, "message": "Mã vạch không hợp lệ!"})
    else:
        return JsonResponse({"success": False, "message": "Chỉ hỗ trợ phương thức POST"})
    

def khuyenmai(request):
        khuyenmais = KhuyenMai.objects.all()
        uudais = UuDaiKhachHang.objects.all()
        sanphams = SanPham.objects.all()
        print(f'khuyenmais: {khuyenmais}')
        print(f'uudais: {uudais}')
        print(f'sanphams: {sanphams}')
        if request.method == 'POST':
            if 'add_company_promotion' in request.POST:
                try:
                    ma_khuyen_mai = request.POST.get('ma_khuyen_mai')
                    ma_san_pham = request.POST.get('ma_san_pham')
                    phan_tram_chiet_khau = float(request.POST.get('phan_tram_chiet_khau'))
                    ngay_bat_dau = request.POST.get('ngay_bat_dau')
                    ngay_ket_thuc = request.POST.get('ngay_ket_thuc')

                    if ma_khuyen_mai and ma_san_pham and phan_tram_chiet_khau and ngay_bat_dau and ngay_ket_thuc:
                        sanpham = get_object_or_404(SanPham, ma_san_pham=ma_san_pham)
                        KhuyenMai.objects.create(
                            ma_khuyen_mai = ma_khuyen_mai,
                            ma_san_pham = sanpham,
                            phan_tram_chiet_khau = phan_tram_chiet_khau,
                            ngay_bat_dau = ngay_bat_dau,
                            ngay_ket_thuc = ngay_ket_thuc
                            )
                        messages.success(request, "Khuyến mãi công ty đã được thêm thành công!")
                        return redirect('khuyenmai')
                    else:
                        messages.error(request, 'Vui lòng điền đầy đủ thông tin!')
                except Exception as e:
                    messages.error(request, f'Lỗi khi tạo khuyến mãi: {e}')
            elif 'add_customer_discount' in request.POST:
                try:
                    ma_khach_hang = request.POST.get('ma_khach_hang')
                    phan_tram_chiet_khau = float(request.POST.get('phan_tram_chiet_khau'))
                    if ma_khach_hang and phan_tram_chiet_khau:
                        UuDaiKhachHang.objects.create(
                            ma_khach_hang = ma_khach_hang,
                            phan_tram_chiet_khau = phan_tram_chiet_khau
                        )
                        messages.success(request, 'Đã thêm ưu đãi khách hàng thành công!')
                        return redirect('khuyenmai')
                    else:
                         messages.error(request, "Vui lòng điền đầy đủ thông tin!")
                except Exception as e:
                    messages.error(request, f"Lỗi khi thêm ưu đãi khách hàng: {e}")
         
        context = {
            'active_menu': 'khuyenmai',
            'khuyenmais': khuyenmais,
            'uudais': uudais,
            'sanphams': sanphams,
        }
        return render(request, 'home/khuyenmai/khuyenmai.html', context)

def mualai(request):
    # Logic cho trang mualai
    return render(request, 'home/mualai/mualai.html', {'active_menu': 'mualai'})

def doanhthu(request):
    # Logic cho trang doanhthu
    return render(request, 'home/doanhthu/doanhthu.html', {'active_menu': 'doanhthu'})

def khaibao(request):
    cacquaybanhangs = QuayBanHang.objects.all()
    if request.method == 'POST':
       if 'add_product' in request.POST:
        try:
             ma_san_pham = request.POST.get('ma_san_pham')
             ten_san_pham = request.POST.get('ten_san_pham')
             gia_ban = request.POST.get('gia_ban')
             quay_hang = request.POST.get('quay_hang')

             if ma_san_pham and ten_san_pham and gia_ban and quay_hang:
                  quay = get_object_or_404(QuayBanHang, ma_quay=quay_hang)
                  SanPham.objects.create(
                      ma_san_pham = ma_san_pham,
                      ten_san_pham = ten_san_pham,
                      gia_ban = gia_ban,
                      quay_hang = quay
                      )
                  messages.success(request, 'Đã thêm sản phẩm thành công!')

             else:
               messages.error(request, 'Vui lòng điền đầy đủ thông tin!')
        except Exception as e:
            messages.error(request, f'Lỗi khi tạo thêm sản phẩm: {e}')
        return redirect('khaibao') # redirect to the same page
    context = {
       'active_menu': 'khaibao',
       'cacquaybanhangs': cacquaybanhangs,
        }
    return render(request, 'home/khaibao/khaibao.html', context) # Changed template path

def dashboard(request):
    # Logic cho trang dashboard
    return render(request, 'home/dashboard/dashboard.html', {'active_menu': 'dashboard'})

def tichdiem(request):
    khach_hangs = KhachHang.objects.all()
    diem_can_de_dat = 100

    khach_hangs_with_points = []
    for khachhang in khach_hangs:
        total_points = khachhang.tichdiem_set.all().aggregate(total_diem=Sum('so_diem'))['total_diem'] or 0
        du_diem_nhan_thuong = total_points >= diem_can_de_dat
        khach_hangs_with_points.append({
            'ma_khach_hang': khachhang.ma_khach_hang,
            'ho_ten': khachhang.ho_ten,
            'total_diem': total_points,
            'du_diem_nhan_thuong': du_diem_nhan_thuong,
            'tong_diem_da_tich_luy': khachhang.tichdiem_set.all().aggregate(total_diem_all=Sum('so_diem'))['total_diem_all'] or 0,
        })

    sanphams = SanPham.objects.filter(ton_kho__gt=0)

    if request.method == 'POST':
        # Kiểm tra mã khách hàng và mã sản phẩm
        if 'add_points' in request.POST:
            try:
                ma_khach_hang = request.POST.get('ma_khach_hang')
                if ma_khach_hang:
                    khachhang = get_object_or_404(KhachHang, ma_khach_hang=ma_khach_hang)
                    TichDiem.objects.create(
                        ma_khach_hang=khachhang,
                        so_diem=10,  # Thêm 10 điểm
                    )
                    messages.success(request, f"Đã thêm 10 điểm cho khách hàng {ma_khach_hang} thành công!")
                else:
                    messages.error(request, 'Lỗi không tìm thấy mã khách hàng!')
                return redirect('tichdiem')
            except Exception as e:
                messages.error(request, f'Lỗi khi thêm điểm: {e}')

        elif 'choose_product' in request.POST:
            try:
                ma_khach_hang_choose = request.POST.get('ma_khach_hang_choose')
                ma_san_pham_choose = request.POST.get('ma_san_pham_choose')
                
                if ma_khach_hang_choose and ma_san_pham_choose:
                    khachhang = get_object_or_404(KhachHang, ma_khach_hang=ma_khach_hang_choose)
                    sanpham = get_object_or_404(SanPham, ma_san_pham=ma_san_pham_choose)

                    total_points = khachhang.tichdiem_set.all().aggregate(total_diem=Sum('so_diem'))['total_diem'] or 0
                    
                    if total_points >= diem_can_de_dat:
                        messages.success(request, f"Bạn đã nhận sản phẩm {sanpham.ten_san_pham} thành công! Số điểm của bạn đã bị trừ {diem_can_de_dat} điểm.")
                        TichDiem.objects.create(
                            ma_khach_hang=khachhang,
                            so_diem=-diem_can_de_dat,
                        )
                    else:
                        messages.error(request, f"Khách hàng {ma_khach_hang_choose} không đủ điểm để nhận sản phẩm!")
                else:
                    messages.error(request, 'Lỗi không tìm thấy mã khách hàng hoặc sản phẩm!')

                return redirect('tichdiem')
            except Exception as e:
                messages.error(request, f"Lỗi khi chọn sản phẩm: {e}")


    context = {
        'active_menu': 'tichdiem',
        'diem_can_de_dat': diem_can_de_dat,
        'khach_hangs': khach_hangs_with_points,
        'sanphams': sanphams,
        'tong_diem': TichDiem.objects.aggregate(Sum('so_diem'))['so_diem__sum'] or 0,
    }
    return render(request, 'home/tichdiem/tichdiem.html', context)