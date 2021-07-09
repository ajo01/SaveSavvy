from userpreferences.models import UserPreference
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Source, Income
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
# Create your views here.


def search_income(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        income = Income.objects.filter(
            amount__istartswith=search_str, owner=request.user) | Income.objects.filter(
            date__istartswith=search_str, owner=request.user) | Income.objects.filter(
            description__icontains=search_str, owner=request.user) | Income.objects.filter(
            source__icontains=search_str, owner=request.user)
        data = income.values()
        return JsonResponse(list(data), safe=False)


@login_required(login_url='/auth/login')
def index(request):
    income = Income.objects.filter(owner=request.user)
    paginator = Paginator(income, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    currency = UserPreference.objects.get(user=request.user).currency
    context = {
        'income': income,
        'page_obj': page_obj,
        'currency': currency
    }
    return render(request, 'income/index.html', context)


@login_required(login_url='/auth/login')
def add_income(request):
    sources = Source.objects.all()
    context = {
        'sources': sources,
        # get access to previous inputs
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'income/add_income.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is a required field')
            return render(request, 'income/add_income.html', context)

        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is a required field')
            return render(request, 'income/add_income.html', context)

    Income.objects.create(owner=request.user,
                          amount=amount, description=description, source=source, date=date)
    messages.success(request, 'Income saved successfully')
    return redirect('income')


@login_required(login_url='/auth/login')
def income_edit(request, id):
    income = Income.objects.get(pk=id)
    sources = Source.objects.all()
    context = {
        'income': income,
        'values': income,
        'sources': sources
    }

    if request.method == 'GET':
        return render(request, 'income/edit_income.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is a required field')
            return render(request, 'income/edit_income.html', context)

        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is a required field')
            return render(request, 'income/edit_income.html', context)

        income.owner = request.user
        income.amount = amount
        income.date = date
        income.source = source
        income.description = description

        income.save()
        messages.success(request, 'Income updated successfully')
        return redirect('income')


@login_required(login_url='/auth/login')
def income_delete(request, id):
    income = Income.objects.get(pk=id)
    income.delete()
    messages.success(request, 'Income removed')
    return redirect('income')
