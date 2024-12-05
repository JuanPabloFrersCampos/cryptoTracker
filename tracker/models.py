from django.db import models

# Create your models here.
class Crypto(models.Model):
    symbol = models.CharField(max_length=4)
    def __str__(self):
        return self.symbol

class Operation(models.Model):
    symbol = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    cryptoQuantity = models.FloatField()
    price = models.FloatField()
    isSell = models.BooleanField()
    def __str__(self):
        symbol = '-' if self.isSell else '+'
        return str(self.symbol) + ' ' + str(symbol) + str(self.cryptoQuantity) + str(' ($') + str(self.cryptoQuantity * self.price) + str(')')