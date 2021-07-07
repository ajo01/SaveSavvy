from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense

# Create your views here.


@login_required(login_url='/auth/login')
def index(request):
    return render(request, 'expenses/index.html')


def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'expenses/add_expense.html', context)
