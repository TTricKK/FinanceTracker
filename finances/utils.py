from django.db.models import Sum
from .models import Transaction

ACCOUNTS = ['savings', 'fire_extinguisher', 'splurge', 'everyday']

def calculate_balances() -> dict:
    # Return current balance for each account as a dictionary
    balances = {}

    for account in ACCOUNTS:
        deposit = Transaction.objects.filter(
            account = account,
            transaction_type = 'deposit'
        ).aggregate(total = Sum('amount'))['total'] or 0

        withdraw = Transaction.objects.filter(
            account = account,
            transaction_type = 'deposit'
        ).aggregate(total = Sum('amount'))['total'] or 0

        balances[account] = deposit - withdraw
        
    return balances