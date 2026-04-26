from django.shortcuts import render
from .models import Transaction
from .utils import calculate_balances

# Create your views here.
def home(request):
    # Display current balance AND transaction history
    balances = calculate_balances()
    transactions = Transaction.objects.all().order_by('-date')

    return render(request, 'finances/home.html', {
        'balances': balances,
        'transaction': transactions,
    })


