from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expense', views.add_expense, name="add-expenses"),
    path('preferences/', include('userpreferences.urls')),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('delete-expense/<int:id>', views.expense_delete, name="expense-delete "),
]
