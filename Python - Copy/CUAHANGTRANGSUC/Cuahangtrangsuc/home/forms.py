# home/forms.py
from django import forms
from Quanlybanhang.models import NhanVien  # Hoặc import từ đúng ứng dụng của bạn
from Quanlybanhang.models import UuDaiKhachHang
from Quanlybanhang.models import KhuyenMai  # Correct import


class NhanVienForm(forms.ModelForm):
    class Meta:
        model = NhanVien
        fields = ['ma_nhan_vien', 'ho_ten']


class KhuyenMaiForm(forms.ModelForm):
    class Meta:
        model = KhuyenMai
        fields = '__all__'

class UuDaiKhachHangForm(forms.ModelForm):
    class Meta:
       model = UuDaiKhachHang
       fields = '__all__'
