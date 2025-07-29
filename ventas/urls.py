from django.urls import path
from .views import registrar_venta

urlpatterns = [
    path('vender/', registrar_venta, name='registrar_venta'),
]
