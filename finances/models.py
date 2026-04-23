from django.db import models

# Create your models here.
class Accounts(models.Model):
    Savings = models.FloatField()
    FireExtinguisher = models.FloatField()
    Splurge = models.FloatField()

    def __str__(self):
        return f"Savings: {self.Savings}, Fire Extinguisher: {self.FireExtinguisher}, Splurge: {self.Splurge}"

class Expenses(models.Model):
    Date = models.DateField()
    Amount = models.FloatField()
    Category = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return f"{self.Date} - {self.Category}: ${self.Amount} - {self.Description}"

