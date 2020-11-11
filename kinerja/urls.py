from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('add_skp/', views.add_skp, name='add_skp'),
    path('test/', views.test, name='test'),
    path('api/pegawai/', views.pegawai_list, name='pegawai_api'),
    path('api/kinerja/', views.kinerja_list, name='kinera_api'),
]