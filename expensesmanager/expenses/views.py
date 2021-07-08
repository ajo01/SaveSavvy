from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages

# Create your views here.


@login_required(login_url='/auth/login')
def index(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    context = {
        'expenses': expenses,
    }
    return render(request, 'expenses/index.html', context)


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
        if not amount:
            messages.error(request, 'Amount is a required field')
            return render(request, 'expenses/add_expense.html', context)

        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is a required field')
            return render(request, 'expenses/add_expense.html', context)

    Expense.objects.create(owner=request.user,
                           amount=amount, description=description, category=category, date=date)
    messages.success(request, 'Expense saved successfully')
    return redirect('expenses')


def expense_edit(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories
    }

    if request.method == 'GET':
        return render(request, 'expenses/edit_expense.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is a required field')
            return render(request, 'expenses/edit_expense.html', context)

        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is a required field')
            return render(request, 'expenses/edit_expense.html', context)

        expense.owner = request.user
        expense.amount = amount
        expense.date = date
        expense.category = category
        expense.description = description

        expense.save()
        messages.success(request, 'Expense updated successfully')
        return redirect('expenses')


def expense_delete(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Expense removed')
    return redirect('expenses')
