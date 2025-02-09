from django.contrib import admin
from django.urls import include, path
from . import views
from .views import duyet_uudai
from .views import delete_uudai
urlpatterns = [
    path('', views.home, name='home'),
    path('quaybanhangs/', views.quaybanhangs, name='quaybanhangs'),
    path('quaybanhang-edit/<str:ma_quay>/', views.quaybanhang_edit, name='quaybanhang-edit'),
    path('quaybanhang-delete/<str:ma_quay>/', views.quaybanhang_delete, name='quaybanhang-delete'),
    path('quaybanhang-new/', views.quaybanhang_new, name='quaybanhang-new'),  
    path('tichdiem/', views.tichdiem, name='tichdiem'),
    path('doanhthu/', views.doanhthu, name='doanhthu'),  # Định nghĩa URL cho Doanh thu
    path('khaibao/', views.khaibao, name='khaibao'),  # Định nghĩa URL cho Doanh thu
    path('dashboard/', views.dashboard, name='dashboard'),  # Định nghĩa URL cho Doanh thu
    path('mualai/', views.mualai, name='mualai'),  # Định nghĩa URL cho Doanh thu
    path('sanpham/', views.sanpham, name='sanpham'),
    path('khuyenmai/', views.khuyenmai, name='khuyenmai'),
    path('khuyenmai/duyet_uudai/<int:id>/', duyet_uudai, name='duyet_uudai'),

    path('quet-barcode/', views.handle_barcode, name='quet_barcode'), 
    path('xu-ly-barcode/', views.handle_barcode, name='handle_barcode'),


    path('nhanviens/', views.nhanviens, name='nhanviens'),
    path('nhanvien-edit/<str:ma_nhan_vien>/', views.nhanvien_delete, name='nhanvien-edit'),
    path('nhanvien-delete/<str:ma_nhan_vien>/', views.nhanvien_delete, name='nhanvien-delete'),



]
