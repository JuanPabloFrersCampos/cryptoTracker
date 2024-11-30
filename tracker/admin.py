from django.contrib import admin
from .models import Crypto, Operation

# Register your models here.

admin.site.register(Crypto)
admin.site.register(Operation)