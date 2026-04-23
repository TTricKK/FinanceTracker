from urllib import request
from django.shortcuts import render
from .models import Accounts

# Create your views here.
def home(request):
    accounts = Accounts.objects.all()
    return render(request, 'finances/home.html',  {'accounts': accounts})


