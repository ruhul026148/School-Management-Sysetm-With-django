from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard')
]