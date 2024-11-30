from django.urls import path
from . import views

# Router

urlpatterns = [
    path('cryptos/', views.indexCryptos),
    path('compra/', views.venta)
]