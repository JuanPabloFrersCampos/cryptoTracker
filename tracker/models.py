from django.db import models
from django.contrib.auth import get_user_model

class Portfolio(models.Model):
    FK_users_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    type = models.IntegerField()
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Crypto(models.Model):
    symbol = models.CharField(max_length=4)
    def __str__(self):
        return self.symbol

class Operation(models.Model):
    symbol = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    FK_portfolio_id = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE
    )
    cryptoQuantity = models.FloatField()
    price = models.FloatField()
    isSell = models.BooleanField()
    def __str__(self):
        symbol = '-' if self.isSell else '+'
        return str(self.symbol) + ' ' + str(symbol) + str(self.cryptoQuantity) + str(' ($') + str(self.cryptoQuantity * self.price) + str(')')