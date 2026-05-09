from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, PasswordResetRequest
from django.contrib import messages


def signup_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect(request.path)

        # duplicate email check
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('home_auth:signup')

        # create user
        user = CustomUser.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        login(request, user)
        messages.success(request, 'Signup Successfully!')
        return redirect('home_auth:login')

    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully!')

            if user.is_superuser:
                return redirect("admin_dashboard")
            elif user.is_staff:
                return redirect("teacher_dashboard")
            else:
                return redirect('dashboard')

        else:
            messages.error(request, 'Invalid Credentials')

    return render(request, 'authentication/login.html')



def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        user = CustomUser.objects.filter(email=email).first()

        if user:
            # delete old tokens
            PasswordResetRequest.objects.filter(user=user).delete()

            reset_request = PasswordResetRequest.objects.create(user=user)
            reset_request.send_reset_email()

            messages.success(request, 'Reset link sent to your email.')
            return redirect('home_auth:login')
        else:
            messages.error(request, 'Email not found')
            return redirect('home_auth:forgot-password')

    return render(request, 'authentication/forgot-password.html')


def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.filter(token=token).first()

    if not reset_request or not reset_request.is_valid():
        messages.error(request, "Invalid or expired reset link")
        return redirect('home_auth:login')

    if request.method == "POST":
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect(request.path)

        user = reset_request.user
        user.set_password(new_password)
        user.save()

        # delete token after use
        reset_request.delete()

        messages.success(request, 'Password reset successfully')
        return redirect('home_auth:login')

    return render(request, 'authentication/reset-password.html', {'token': token})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home_auth:login')