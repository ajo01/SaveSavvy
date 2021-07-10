from django.urls import path
from django.urls.conf import include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expense', views.add_expense, name="add-expenses"),
    path('preferences/', include('userpreferences.urls')),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('delete-expense/<int:id>', views.expense_delete, name="expense-delete"),
    path('search-expenses', csrf_exempt(views.search_expenses),
         name="search-expenses"),
    path('expense-summary', views.expense_category_summary, name="expense-summary"),
    path('expense-stats', views.stats_view, name="expense-stats"),
    path('export-csv', views.export_csv, name="export-csv"),
]
