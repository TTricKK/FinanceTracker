from django.db import models

# Create your models here.
class Transaction(models.Model):

    ACCOUNT_CHOICES = [
        ('savings', 'Savings'),
        ('fire_extinguisher', 'Fire Extinguisher'),
        ('splurge', 'Splurge'),
        ('everyday', 'Everyday'),
    ]

    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),     # money in
        ('withdraw', 'Withdraw'),   # money out
    ]

    account = models.CharField(max_length = 20, choices = ACCOUNT_CHOICES)
    transaction_type = models.CharField(max_length = 10, choices = TRANSACTION_TYPES)
    
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    date = models.DateField()
    description = models.CharField(max_length = 255, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f"{self.date} | {self.account} | {self.transaction_type} | {self.amount}"

