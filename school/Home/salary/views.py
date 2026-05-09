from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Salary


# ===== Add Salary =====
def add_salary(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        joining_date = request.POST.get('joining_date')
        amount = request.POST.get('amount')

        Salary.objects.create(
            staff_id=staff_id,
            name=name,
            gender=gender,
            joining_date=joining_date,
            amount=amount
        )

        messages.success(request, "Salary added successfully")
        return redirect("salary_list")

    return render(request, "salary/add-salary.html")


# ===== Salary List =====
def salary_list(request):
    salary_list = Salary.objects.all().order_by('-created_at')

    context = {
        'salary_list': salary_list
    }

    return render(request, "salary/salary.html", context)