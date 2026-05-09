from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher
from django.contrib import messages


# ===== Add Teacher =====
def add_teacher(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        mobile = request.POST.get('mobile')
        joining_date = request.POST.get('joining_date')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')

        # Login
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Address
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')

        teacher_image = request.FILES.get('teacher_image')

        Teacher.objects.create(
            teacher_id=teacher_id,
            name=name,
            gender=gender,
            date_of_birth=date_of_birth,
            mobile=mobile,
            joining_date=joining_date,
            qualification=qualification,
            experience=experience,
            username=username,
            email=email,
            password=password,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            teacher_image=teacher_image
        )

        messages.success(request, "Teacher added successfully")

    return render(request, "teachers/add-teacher.html")


# ===== Teacher List =====
def teacher_list(request):
    teacher_list = Teacher.objects.all()
    context = {
        'teacher_list': teacher_list
    }
    return render(request, "teachers/teachers.html", context)


# ===== Edit Teacher =====
def edit_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)

    if request.method == "POST":
        teacher.teacher_id = request.POST.get('teacher_id')
        teacher.name = request.POST.get('name')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.mobile = request.POST.get('mobile')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.qualification = request.POST.get('qualification')
        teacher.experience = request.POST.get('experience')

        teacher.username = request.POST.get('username')
        teacher.email = request.POST.get('email')
        teacher.password = request.POST.get('password')

        teacher.address = request.POST.get('address')
        teacher.city = request.POST.get('city')
        teacher.state = request.POST.get('state')
        teacher.zip_code = request.POST.get('zip_code')
        teacher.country = request.POST.get('country')
         # ✅ image handling fix
        if request.FILES.get('teacher_image'):
            teacher.teacher_image = request.FILES.get('teacher_image')

        teacher.save()

        return redirect("teacher_list")

    return render(request, "teachers/edit-teacher.html", {'teacher': teacher})


# ===== View Teacher =====
def view_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    context = {
        'teacher': teacher
    }
    return render(request, "teachers/teacher-details.html", context)


# ===== Delete Teacher =====
def delete_teacher(request, slug):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher, slug=slug)
        teacher.delete()
        return redirect('teacher_list')

    return HttpResponseForbidden()
