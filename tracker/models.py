from django.db import models

# Create your models here.
class Crypto(models.Model):
    symbol = models.CharField(max_length=4)
    def __str__(self):
        return self.symbol

class Operation(models.Model):
    symbol = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    cryptoQuantity = models.DecimalField(max_digits=20, decimal_places=8)
    operationValue = models.DecimalField(max_digits=8, decimal_places=2)
    isPurchase = models.BooleanField()
    #class Meta:
    #    abstract = True
    def __str__(self):
        return self.symbol