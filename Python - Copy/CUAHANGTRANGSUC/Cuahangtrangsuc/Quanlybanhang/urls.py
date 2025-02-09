from django.urls import path
from . import views

urlpatterns = [
    path('nhanviens/', views.nhanviens, name='nhanviens'),
    path('nhanvien-edit/<str:ma_nhan_vien>/', views.nhanvien_edit, name='nhanvien-edit'),
    path('nhanvien-delete/<str:ma_nhan_vien>/', views.nhanvien_delete, name='nhanvien-delete'),
    path('nhanvien-new/', views.nhanvien_new, name='nhanvien-new'),
    path('san-pham-list/', views.san_pham_list, name='san-pham-list'),
    path('khuyen-mai-list/', views.khuyen_mai_list, name='khuyen-mai-list'),
    path('gia-vang-list/', views.gia_vang_list, name='gia-vang-list'),
    path('hoa-don-list/', views.hoa_don_list, name='hoa-don-list'),
    path('chi-tiet-hoa-don-list/', views.chi_tiet_hoa_don_list, name='chi-tiet-hoa-don-list'),

    path('quaybanhang-edit/<str:ma_quay>/', views.quaybanhang_edit, name='quaybanhang-edit'),
    path('quaybanhangs/', views.quaybanhangs, name='quaybanhangs'),
]