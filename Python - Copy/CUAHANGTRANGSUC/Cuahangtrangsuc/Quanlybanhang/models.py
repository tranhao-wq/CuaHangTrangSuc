from django.db import models

# Create your models here.

class HoaDon(models.Model):
    ma_hoa_don = models.CharField(max_length=20, primary_key=True) 
    ngay_lap = models.DateTimeField()  
    tong_tien = models.DecimalField(max_digits=10, decimal_places=2)  
    ma_khach_hang = models.CharField(max_length=20)  


    def __str__(self):
        return f'Hóa đơn {self.ma_hoa_don} - {self.ngay_lap}'
    
class ChiTietHoaDon(models.Model):
    id = models.AutoField(primary_key=True)  
    ma_hoa_don = models.ForeignKey('HoaDon', on_delete=models.CASCADE)  
    ma_san_pham = models.ForeignKey('SanPham', on_delete=models.CASCADE)  
    so_luong = models.IntegerField()  
    don_gia = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f'Chi tiết hóa đơn {self.ma_hoa_don} - Sản phẩm {self.ma_san_pham}'

class NhanVien(models.Model):
    ma_nhan_vien = models.CharField(max_length=20, primary_key=True)
    ho_ten = models.CharField(max_length=100)
    quay_lam_viec = models.ForeignKey(
       'QuayBanHang',
       on_delete=models.SET_NULL,
       null=True,
       blank=True,
       related_name='nhan_vien_quay_lam_viec'
    )

    def __str__(self):
       return self.ho_ten
    
class KhachHang(models.Model):
    ma_khach_hang = models.CharField(max_length=20, primary_key=True)  
    ho_ten = models.CharField(max_length=100)  
    sdt = models.CharField(max_length=15)  

    def __str__(self):
        return self.ho_ten

class SanPham(models.Model):
    ma_san_pham = models.CharField(max_length=100, primary_key=True)
    ten_san_pham = models.CharField(max_length=255)
    gia_ban = models.DecimalField(max_digits=10, decimal_places=2)
    ton_kho = models.IntegerField()

    def __str__(self):
        return self.ten_san_pham

class LoaiSanPham(models.Model):
    ma_loai_san_pham = models.CharField(max_length=20, primary_key=True)  
    ten_loai_san_pham = models.CharField(max_length=100)  

    def __str__(self):
        return self.ten_loai_san_pham

class KhuyenMai(models.Model):
    ma_khuyen_mai = models.CharField(max_length=20, primary_key=True)  
    ma_san_pham = models.ForeignKey('SanPham', on_delete=models.CASCADE)  
    phan_tram_chiet_khau = models.DecimalField(max_digits=5, decimal_places=2)  
    ngay_bat_dau = models.DateTimeField()  
    ngay_ket_thuc = models.DateTimeField()  

    def __str__(self):
        return f'Khuyến mãi {self.ma_khuyen_mai} - {self.ma_san_pham.ten_san_pham}'
    
class GiaVang(models.Model):
    id = models.AutoField(primary_key=True)  
    thoi_gian = models.DateTimeField()  
    gia_vang_24k = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f'Giá vàng 24K tại {self.thoi_gian} - {self.gia_vang_24k} VND'
    
class QuayBanHang(models.Model):
    ma_quay = models.CharField(max_length=20, primary_key=True)  
    ten_quay = models.CharField(max_length=100)
    nhan_vien_phu_trach = models.ForeignKey(NhanVien, on_delete=models.SET_NULL, null=True, blank=True)
    san_phams = models.ManyToManyField(SanPham, related_name='quays')

    def __str__(self):
        return self.ten_quay

class MuaLai(models.Model):
    id = models.AutoField(primary_key=True)
    ngay_mua_lai = models.DateTimeField()
    gia_mua_lai = models.DecimalField(max_digits=10, decimal_places=2)
    ghi_chu = models.TextField(null=True, blank=True)

    hoa_don = models.ForeignKey('HoaDon', on_delete=models.CASCADE, to_field='ma_hoa_don')
    san_pham = models.ForeignKey('SanPham', on_delete=models.CASCADE, to_field='ma_san_pham')

    def __str__(self):
        return f'Mua lại {self.id} cho Hóa đơn {self.hoa_don} - Sản phẩm {self.san_pham}'


class UuDaiKhachHang(models.Model):
    id = models.AutoField(primary_key=True)
    ma_khach_hang = models.CharField(max_length=20)
    phan_tram_chiet_khau = models.DecimalField(max_digits=5, decimal_places=2)
    duoc_duyet = models.BooleanField(default=False)

    def __str__(self):
        return f'Ưu đãi cho khách hàng {self.ma_khach_hang} - Chiết khấu {self.phan_tram_chiet_khau}'

class TichDiem(models.Model):
    ma_khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    so_diem = models.IntegerField()
    thoi_gian_tich_diem = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f'Tích điểm cho khách hàng {self.ma_khach_hang.ma_khach_hang} - {self.so_diem} điểm'