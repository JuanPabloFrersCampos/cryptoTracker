from django.contrib import admin
from .models import Crypto, Operation, Portfolio

# Register your models here.

admin.site.register(Crypto)
admin.site.register(Operation)
admin.site.register(Portfolio)