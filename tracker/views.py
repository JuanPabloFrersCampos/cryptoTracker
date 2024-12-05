from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .models import Crypto
import json
from .forms import cryptoOperationForm
from .dao import Dao
from .walletOverviewService import WalletOverviewService

class IndexCryptosView(View):
    def get(self, request):
        cryptos_list = Crypto.objects.all()
        return render(request, "availableCryptos.html", {"cryptos_list": cryptos_list})

class OperationView(View):
    def get(self, request):
        form = cryptoOperationForm()
        return render(request, "cryptoOperation.html", {"form": form})

    def post(self, request):
        form = cryptoOperationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Created')
        return render(request, "cryptoOperation.html", {"form": form})

class WalletView(View):
    def get(self, request):
        dao = Dao()
        walletOverviewService = WalletOverviewService()
        operationsBySimbol = dao.get_all_operations_grouping_by_symbol()
        walletOverview = walletOverviewService.process(operationsBySimbol)
        return render(request, "walletOverview.html", {"walletOverview": walletOverview})
    
class WalletViewApi(View):
    def get(self, request):
        dao = Dao()
        walletOverviewService = WalletOverviewService()
        operationsBySimbol = dao.get_all_operations_grouping_by_symbol()
        walletOverview = walletOverviewService.process(operationsBySimbol)
        return HttpResponse(
            json.dumps(walletOverview),
            content_type="application/json"
        )