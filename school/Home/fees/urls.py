from django.urls import path
from . import views

urlpatterns = [
    path("", views.fees_list, name="fees_list"),
    path("add/", views.add_fees, name="add_fees"),
    path("fees/<str:slug>/", views.view_fees, name="view_fees"),
    path("edit/<str:slug>/", views.edit_fees, name="edit_fees"),
    path("delete/<str:slug>/", views.delete_fees, name="delete_fees"),
]