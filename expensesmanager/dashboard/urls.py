from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    # path('stats', views.stats, name="dashboard-stats"),
]
