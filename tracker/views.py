from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Crypto, Operation
from django.template import loader
from .forms import cryptoOperationForm
from .dao import dao #inyectar
from .walletOverviewService import WalletOverviewService

# Create your views here.
# Views = HTTP Handlers

def indexCryptos(request):
    cryptos_list = Crypto.objects.all()
    template = loader.get_template("availableCryptos.html")
    context = {
        "cryptos_list": cryptos_list
    }
    return HttpResponse(template.render(context, request))

def operation(request):
    if request.method == 'POST':
        form = cryptoOperationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Created')
    else:
        form = cryptoOperationForm()
    return render(request, "cryptoOperation.html", {"form": form})

def wallet(request):
    operationsBySimbol = dao.get_all_operations_grouping_by_symbol()
    walletOverviewService = WalletOverviewService()
    walletOverview = walletOverviewService.process(operationsBySimbol)
    context = {
        "walletOverview": walletOverview
    }
    return render(request, "walletOverview.html", context)