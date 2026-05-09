from django.urls import path
from . import views

urlpatterns = [
    path("", views.exam_list, name="exam_list"),
    path("add/", views.add_exam, name="add_exam"),
    path("exam/<str:slug>/", views.view_exam, name="view_exam"),
    path("edit/<str:slug>/", views.edit_exam, name="edit_exam"),
    path("delete/<str:slug>/", views.delete_exam, name="delete_exam"),
]