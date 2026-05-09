from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject
from django.contrib import messages


# ===== Add Subject =====
from django.utils.text import slugify

def add_subject(request):
    print("VIEW HIT")

    if request.method == "POST":
        print("POST RECEIVED")

        subject_name = request.POST.get('subject_name')

        Subject.objects.create(
            subject_id=request.POST.get('subject_id'),
            subject_name=subject_name,
            student_class=request.POST.get('student_class'),
            slug=slugify(subject_name)   # ✅ ADD THIS
        )

        messages.success(request, "Subject added successfully")
        return redirect('subject_list')

    return render(request, "subjects/add-subject.html")
# ===== Subject List =====
def subject_list(request):
    subject_list = Subject.objects.all()
    context = {
        'subject_list': subject_list
    }
    return render(request, "subjects/subjects.html", context)


# ===== Edit Subject =====
def edit_subject(request, id):
    subject = get_object_or_404(Subject, id=id)

    if request.method == "POST":
        subject.subject_id = request.POST.get('subject_id')
        subject.subject_name = request.POST.get('subject_name')
        subject.student_class = request.POST.get('student_class')

        subject.save()
        return redirect("subject_list")

    return render(request, "subjects/edit-subject.html", {'subject': subject})


# ===== View Subject =====
def view_subject(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    context = {
        'subject': subject
    }
    return render(request, "subjects/subject-details.html", context)


# ===== Delete Subject =====
def delete_subject(request, slug):
    if request.method == "POST":
        subject = get_object_or_404(Subject, slug=slug)
        subject.delete()
        return redirect('subject_list')

    return HttpResponseForbidden()