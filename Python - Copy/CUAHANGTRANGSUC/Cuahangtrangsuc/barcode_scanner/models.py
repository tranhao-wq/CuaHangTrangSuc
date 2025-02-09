from django.db import models

class SanPham(models.Model):
    ma_san_pham = models.CharField(max_length=20, primary_key=True)
    ten_san_pham = models.CharField(max_length=100)
    gia_ban = models.DecimalField(max_digits=10, decimal_places=2)
    ton_kho = models.IntegerField()

    def __str__(self):
        return self.ten_san_pham
