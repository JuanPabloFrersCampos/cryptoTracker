from django.urls import path
from .views import IndexCryptosView, OperationView, WalletView, portfolioEndpoint

urlpatterns = [
    path('cryptos/', IndexCryptosView.as_view()),
    path('operation/', OperationView.as_view()),
    path('wallet/', WalletView.as_view()),
    path('wallet/api', portfolioEndpoint.as_view(), name='wallet_api'),
]