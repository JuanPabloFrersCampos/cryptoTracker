from django import forms
from django.forms import ModelForm
from .models import Operation

class cryptoOperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = ["symbol", "cryptoQuantity", "price", "isSell"]