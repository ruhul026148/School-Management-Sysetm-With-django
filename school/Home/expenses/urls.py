from django.urls import path
from . import views

urlpatterns = [
    path("", views.expenses_list, name="expenses_list"),
    path("add/", views.add_expenses, name="add_expenses"),
]