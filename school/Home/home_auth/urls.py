from django.urls import path
from .views import signup_view, login_view, forgot_password_view, reset_password_view, logout_view

app_name = "home_auth"

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password_view, name='forgot-password'),
    path('reset-password/<str:token>/', reset_password_view, name='reset-password'),
    path('logout/', logout_view, name='logout'),
]