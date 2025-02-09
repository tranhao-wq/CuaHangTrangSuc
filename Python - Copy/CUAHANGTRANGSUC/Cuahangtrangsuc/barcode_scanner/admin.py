from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SanPham

@admin.register(SanPham)
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('ma_san_pham', 'ten_san_pham', 'gia_ban', 'ton_kho')
    change_form_template = "admin/barcode_scanner/sanpham_change_form.html"
