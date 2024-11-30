from django.shortcuts import render
from django.http import HttpResponse
from .models import Crypto, Operation
from django.template import loader

# Create your views here.
# Views = HTTP Handlers

def indexCryptos(request):
    cryptos_list = Crypto.objects.all()
    template = loader.get_template("availableCryptos.html")
    context = {
        "cryptos_list": cryptos_list
    }
    return HttpResponse(template.render(context, request))

def venta(request):
    return render(request, 'venta.html')