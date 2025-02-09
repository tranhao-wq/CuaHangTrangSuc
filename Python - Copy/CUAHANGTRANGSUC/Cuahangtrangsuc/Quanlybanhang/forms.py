from django import forms
from .models import QuayBanHang, NhanVien, SanPham
from .models import UuDaiKhachHang
from Quanlybanhang.models import NhanVien, SanPham  # Import model NhanVien và SanPham từ Quanlybanhang

class QuayBanHangForm(forms.ModelForm):
    class Meta:
        model = QuayBanHang
        fields = ['ten_quay', 'ma_quay']
        widgets = {
            'ten_quay': forms.TextInput(attrs={
                'class': 'form-control form-control-lg custom-input',
                'placeholder': 'Nhập tên quầy',
            }),
            'ma_quay': forms.TextInput(attrs={
                'class': 'form-control form-control-lg custom-input',
                'placeholder': 'Nhập mã quầy',
            }),
        }
    def clean_ma_quay(self):
        ma_quay = self.cleaned_data.get('ma_quay')
        if not ma_quay.isdigit():
            raise forms.ValidationError("Mã quầy phải là số")
        return ma_quay


class NhanVienForm(forms.ModelForm):
    class Meta:
        model = NhanVien
        fields = ['ma_nhan_vien', 'ho_ten']
        widgets = {
            'ma_nhan_vien': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mã nhân viên'}),
            'ho_ten': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ tên'}),
        }
    ma_nhan_vien = forms.CharField(label="Mã nhân viên", max_length=20)
    ho_ten = forms.CharField(label="Họ tên", max_length=100)

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['ma_san_pham', 'ten_san_pham', 'gia_ban', 'ton_kho']
        widgets = {
            'ma_san_pham': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mã sản phẩm'}),
            'ten_san_pham': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên sản phẩm'}),
            'gia_ban': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nhập giá bán'}),
            'ton_kho': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nhập số lượng tồn kho'}),
        }
    ma_san_pham = forms.CharField(label="Mã sản phẩm", max_length=20)
    ten_san_pham = forms.CharField(label="Tên sản phẩm", max_length=100)
    gia_ban = forms.DecimalField(label="Giá bán", max_digits=10, decimal_places=2)
    ton_kho = forms.IntegerField(label="Tồn kho")

class KhuyenMai(forms.Form):  # Hoặc class KhuyenMai(models.Model) nếu là model
    # Các trường của form
    ten_khuyen_mai = forms.CharField(max_length=100)
    ngay_bat_dau = forms.DateField()
    ngay_ket_thuc = forms.DateField()

class UuDaiKhachHang(forms.Form):
    ten_uu_dai = forms.CharField(max_length=100)
    gia_tri = forms.DecimalField(max_digits=10, decimal_places=2)
    ngay_bat_dau = forms.DateField()
    ngay_ket_thuc = forms.DateField()