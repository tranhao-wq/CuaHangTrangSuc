from django.db import models

from Quanlybanhang.models import KhachHang

# Create your models here.

class UuDaiKhachHang(models.Model):
    id = models.AutoField(primary_key=True)
    ma_khach_hang = models.CharField(max_length=20)
    phan_tram_chiet_khau = models.DecimalField(max_digits=5, decimal_places=2)
    duoc_duyet = models.BooleanField(default=False)

    def __str__(self):
      return f'Ưu đãi cho khách hàng {self.ma_khach_hang} - Chiết khấu {self.phan_tram_chiet_khau}'
class HoaDon(models.Model):
    so_hoa_don = models.CharField(max_length=100)
    ngay_lap = models.DateTimeField()
    tong_tien = models.DecimalField(max_digits=10, decimal_places=2)
    # Các trường khác

    def __str__(self):
        return self.so_hoa_don
    
class QuayBanHang(models.Model):
    ten_quay = models.CharField(max_length=100)
    vi_tri = models.CharField(max_length=255)
    # Các trường khác

    def __str__(self):
        return self.ten_quay
    
class NhanVien(models.Model):
    ten_nhan_vien = models.CharField(max_length=100)
    chuc_vu = models.CharField(max_length=100)
    # Các trường khác

    def __str__(self):
        return self.ten_nhan_vien
    
class ChiTietHoaDon(models.Model):
    # Định nghĩa các trường dữ liệu ở đây
    hoa_don = models.ForeignKey('HoaDon', on_delete=models.CASCADE)
    san_pham = models.CharField(max_length=100)
    so_luong = models.IntegerField()

    def __str__(self):
        return f"ChiTietHoaDon {self.id}"
    


class SanPham(models.Model):
    ma_san_pham = models.CharField(max_length=20, primary_key=True)
    ten_san_pham = models.CharField(max_length=255)
    gia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ten_san_pham

class KhuyenMai(models.Model):
    ma_khuyen_mai = models.CharField(max_length=20, primary_key=True)
    ma_san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    phan_tram_chiet_khau = models.DecimalField(max_digits=5, decimal_places=2)
    ngay_bat_dau = models.DateTimeField()
    ngay_ket_thuc = models.DateTimeField()

    def __str__(self):
        return f'Khuyến mãi {self.ma_khuyen_mai} - {self.ma_san_pham.ten_san_pham}'
