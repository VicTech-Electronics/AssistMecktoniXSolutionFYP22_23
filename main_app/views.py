from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from main_app.models import Customer, Transaction, Due
from .decorators import unauthenticated
from django.contrib.auth.models import User
from django.db.models import Q
import json

# Create your views here.
@login_required(login_url='login')
def home(request):
    # Count costomers from the model
    no_of_customers = Customer.objects.all().count()

    # Count revenue from the model
    transaction_amount = 0
    for transaction in Transaction.objects.all():
        transaction_amount = transaction_amount + transaction.amount

    # Count expenses from the model
    due_amount = 0
    for due in Due.objects.all():
        due_amount = due_amount + due.amount

    # Calculate monthly transactions
    monthly_transactions = 0
    monthly_transactions_amount = []
    for month in range(1, 13):
        for transaction in Transaction.objects.filter(date_time__month=month):
            monthly_transactions = monthly_transactions + transaction.amount
        monthly_transactions_amount.append(monthly_transactions)
        monthly_transactions = 0
    
    # Calculate monthly due
    monthly_due = 0
    monthly_due_amount = []
    for month in range(1, 13):
        for due in Due.objects.filter(date_time__month=month):
            monthly_due = monthly_due + due.amount
        monthly_due_amount.append(monthly_due)
        monthly_due = 0

    # Collect monthly data for revenue and expenses
    data = {
        'no_of_customers': no_of_customers,
        'transactions': transaction_amount,
        'due': due_amount,
    }

    return render(request, 'index.html', {'data': data,})

@unauthenticated
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Hello {username}, you are successfull login')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        meter_number = request.POST.get('meter_number')
        
        if Customer.objects.filter(meter_number=meter_number).exists():
            messages.error(request, 'Meter number alread in use')
            return redirect('register')

        user = User.objects.create(username=username)
        user.save()
        customer = Customer.objects.create(user=user, meter_number=meter_number)
        customer.save()
        messages.success(request, f'{username}, Registered successful')
        return redirect('register')

    return render(request, 'register.html')



def payment(request):
    if request.method == 'POST':
        meter_number = request.POST.get('meter_number')
        amount = request.POST.get('amount')

        if Customer.objects.filter(meter_number = meter_number).exists():
            customer = Customer.objects.get(meter_number=meter_number)

            if Transaction.objects.filter(customer=customer).exists():
                transaction = Transaction.objects.get(customer=customer)
                transaction.amount += float(amount)
                transaction.save()
            else:
                transaction = Transaction.objects.create(customer=customer, amount=amount)
                transaction.save()

            transaction = Transaction.objects.get(customer=customer)
            due = Due.objects.get(customer=customer)

            remaining_amount = due.amount - transaction.amount
            due.amount = remaining_amount
            due.save()

            messages.success(request, f'Hello {customer.user.username}, you have done successful payment')
            return redirect('payment')

        else:
            messages.error(request, 'Sorry! Meter number not exist')
            return redirect('payment')
    
    return render(request, 'payment.html')