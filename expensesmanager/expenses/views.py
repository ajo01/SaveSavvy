from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages

# Create your views here.


@login_required(login_url='/auth/login')
def index(request):
    return render(request, 'expenses/index.html')


def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        # get access to previous inputs
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        if not amount or description:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'expenses/add_expense.html', context)

        return render(request, 'expenses/add_expense.html', context)
