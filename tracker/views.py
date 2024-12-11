from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from tracker.portfolio.portfolio_endpoint_handler import PortfolioEndpointHandler
from .models import Crypto
import json
from .forms import cryptoOperationForm
from .dao import Dao

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
    
class portfolioEndpoint(View):
    def get(self, request: HttpRequest):
        handler = PortfolioEndpointHandler(self.request)
        portfolio_summary = handler.process()
        portfolio_summary_dict = portfolio_summary.to_dict()
        return HttpResponse(
            json.dumps(portfolio_summary_dict),
            content_type="application/json"
        )