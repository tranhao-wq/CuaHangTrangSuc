from django.contrib import admin
from .models import *
from .models import (
    QuayBanHang,
    NhanVien,
    KhachHang,
    LoaiSanPham,
    SanPham,
    GiaVang,
    HoaDon,
    ChiTietHoaDon,
    KhuyenMai,
    MuaLai,
)

@admin.register(HoaDon)
class HoaDonAdmin(admin.ModelAdmin):
    list_display = ('ma_hoa_don', 'ngay_lap', 'tong_tien', 'ma_khach_hang')
    search_fields = ('ma_hoa_don', 'ma_khach_hang')
    list_filter = ('ngay_lap',)

@admin.register(ChiTietHoaDon)
class ChiTietHoaDonAdmin(admin.ModelAdmin):
    list_display = ('id', 'ma_hoa_don', 'ma_san_pham', 'so_luong', 'don_gia')
    search_fields = ('ma_hoa_don__ma_hoa_don', 'ma_san_pham__ten_san_pham')
    list_filter = ('ma_hoa_don__ma_hoa_don', 'ma_san_pham__ten_san_pham')

    # Tùy chọn thêm các phương thức để hiển thị thông tin cho các khóa ngoại
    def ma_hoa_don(self, obj):
        return obj.ma_hoa_don.ma_hoa_don  # Trả về mã hóa đơn từ HoaDon

    def ma_san_pham(self, obj):
        return obj.ma_san_pham.ten_san_pham  # Trả về tên sản phẩm từ SanPham

@admin.register(NhanVien)
class NhanVienAdmin(admin.ModelAdmin):
   list_display = ('ma_nhan_vien', 'ho_ten', 'quay_lam_viec')
   # Để hiển thị và chỉnh sửa trường quay_lam_viec trực tiếp
   fields = ('ma_nhan_vien', 'ho_ten', 'quay_lam_viec')
    # hoặc có thể dùng fieldsets để nhóm các field
   #fieldsets = (
    #   ('Thông tin nhân viên', {'fields': ('ma_nhan_vien', 'ho_ten')}),
    #   ('Thông tin quầy làm việc', {'fields': ('quay_lam_viec',)}),
    #)
   search_fields = ('ma_nhan_vien','ho_ten')

@admin.register(KhachHang)
class KhachHangAdmin(admin.ModelAdmin):
    list_display = ('ma_khach_hang', 'ho_ten', 'sdt')
    search_fields = ('ho_ten', 'sdt')

@admin.register(SanPham)
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('ma_san_pham', 'ten_san_pham', 'gia_ban', 'ton_kho')
    search_fields = ('ten_san_pham',)
    list_filter = ('ton_kho',)

@admin.register(LoaiSanPham)
class LoaiSanPhamAdmin(admin.ModelAdmin):
    list_display = ('ma_loai_san_pham', 'ten_loai_san_pham')
    search_fields = ('ten_loai_san_pham',)

@admin.register(KhuyenMai)
class KhuyenMaiAdmin(admin.ModelAdmin):
    list_display = ('ma_khuyen_mai', 'ma_san_pham', 'phan_tram_chiet_khau', 'ngay_bat_dau', 'ngay_ket_thuc')
    search_fields = ('ma_khuyen_mai', 'ma_san_pham__ten_san_pham')
    list_filter = ('ngay_bat_dau', 'ngay_ket_thuc')

@admin.register(GiaVang)
class GiaVangAdmin(admin.ModelAdmin):
    list_display = ('id', 'thoi_gian', 'gia_vang_24k')
    list_filter = ('thoi_gian',)

@admin.register(QuayBanHang)
class QuayBanHangAdmin(admin.ModelAdmin):
   list_display = ('ma_quay','ten_quay','nhan_vien_phu_trach')
   search_fields = ('ma_quay','ten_quay')

@admin.register(MuaLai)
class MuaLaiAdmin(admin.ModelAdmin):
    list_display = ('id', 'hoa_don', 'san_pham', 'ngay_mua_lai', 'gia_mua_lai', 'ghi_chu')
    search_fields = ('hoa_don__ma_hoa_don', 'san_pham__ten_san_pham')
    list_filter = ('ngay_mua_lai',)


@admin.register(UuDaiKhachHang)
class UuDaiKhachHangAdmin(admin.ModelAdmin):
    list_display = ('id', 'ma_khach_hang', 'phan_tram_chiet_khau', 'duoc_duyet')
    search_fields = ('ma_khach_hang',)
    list_filter = ('duoc_duyet',)

@admin.register(TichDiem)
class TichDiemAdmin(admin.ModelAdmin):
    list_display = ('id','ma_khach_hang', 'so_diem', 'thoi_gian_tich_diem')
    list_filter = ('ma_khach_hang',)
    search_fields = ('ma_khach_hang__ma_khach_hang',)

    def ma_khach_hang(self, obj):
        return obj.ma_khach_hang.ma_khach_hang