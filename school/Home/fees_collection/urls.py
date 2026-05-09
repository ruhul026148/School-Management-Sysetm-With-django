from django.urls import path
from . import views

urlpatterns = [
    path("", views.fees_collection_list, name="fees_collection_list"),
    path("add/", views.add_fees, name="add_fees_collection"),
]