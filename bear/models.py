from django.db import models
from .constants import PROFILE_CHOICES


class Player(models.Model):

    name = models.CharField(max_length=40)
    document= models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15)
    date_birth = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    profile = models.CharField(max_length=2, choices=PROFILE_CHOICES, default='N')

    def __str__(self):
        return self.name
    
class Deposit(models.Model):
    value= models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    balance_after = models.DecimalField(max_digits=10, decimal_places=2)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Deposito criado em {self.date_created}'