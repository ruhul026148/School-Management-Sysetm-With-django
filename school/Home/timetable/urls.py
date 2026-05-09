from django.urls import path
from . import views

urlpatterns = [
    path("", views.timetable_list, name="timetable_list"),
    path("add/", views.add_timetable, name="add_timetable"),
    path("timetable/<str:slug>/", views.view_timetable, name="view_timetable"),
    path("edit/<str:slug>/", views.edit_timetable, name="edit_timetable"),
    path("delete/<str:slug>/", views.delete_timetable, name="delete_timetable"),
]