from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from django.contrib import messages


# ===== Add Department =====
def add_department(request):
    if request.method == "POST":
        department_id = request.POST.get('department_id')
        department_name = request.POST.get('department_name')
        head_of_department = request.POST.get('head_of_department')
        department_start_date = request.POST.get('department_start_date')
        no_of_students = request.POST.get('no_of_students')

        Department.objects.create(
            department_id=department_id,
            department_name=department_name,
            head_of_department=head_of_department,
            department_start_date=department_start_date,
            no_of_students=no_of_students
        )

        messages.success(request, "Department added successfully")
        return redirect("department_list")   # ✅ redirect added

    return render(request, "departments/add-department.html")


# ===== Department List =====
def department_list(request):
    department_list = Department.objects.all()
    context = {
        'department_list': department_list
    }
    return render(request, "departments/departments.html", context)


# ===== Edit Department =====
def edit_department(request, slug):
    department = get_object_or_404(Department, slug=slug)

    if request.method == "POST":
        department.department_id = request.POST.get('department_id')
        department.department_name = request.POST.get('department_name')
        department.head_of_department = request.POST.get('head_of_department')
        department.department_start_date = request.POST.get('department_start_date')
        department.no_of_students = request.POST.get('no_of_students')

        department.save()
        return redirect("department_list")

    return render(request, "departments/edit-department.html", {'department': department})


# ===== View Department =====
def view_department(request, slug):
    department = get_object_or_404(Department, slug=slug)
    context = {
        'department': department
    }
    return render(request, "departments/department-details.html", context)


# ===== Delete Department =====
def delete_department(request, slug):
    if request.method == "POST":
        department = get_object_or_404(Department, slug=slug)
        department.delete()
        return redirect('department_list')

    return HttpResponseForbidden()