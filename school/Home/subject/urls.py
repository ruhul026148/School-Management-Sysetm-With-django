from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.subject_list, name="subject_list"),
    path("add/", views.add_subject, name="add_subject"),
    path("subject/<str:slug>/", views.view_subject, name="view_subject"),
    path('subject/edit/<int:id>/', views.edit_subject, name='edit_subject'),
    path("delete/<str:slug>/", views.delete_subject, name="delete_subject"),
]