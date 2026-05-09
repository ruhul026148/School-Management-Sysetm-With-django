from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Exam
from subject.models import Subject
from django.contrib import messages


# ===== Add Exam =====
def add_exam(request):
    subjects = Subject.objects.all()   # dropdown এর জন্য

    if request.method == "POST":
        exam_name = request.POST.get('exam_name')
        subject_id = request.POST.get('subject')  # subject id আসবে form থেকে
        fees = request.POST.get('fees')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        event_date = request.POST.get('event_date')

        subject = get_object_or_404(Subject, id=subject_id)

        Exam.objects.create(
            exam_name=exam_name,
            subject=subject,
            fees=fees,
            start_time=start_time,
            end_time=end_time,
            event_date=event_date
        )

        messages.success(request, "Exam added successfully")
        return redirect("exam_list")

    return render(request, "exams/add-exam.html", {'subjects': subjects})


# ===== Exam List =====
def exam_list(request):
    exam_list = Exam.objects.select_related('subject').all()
    context = {
        'exam_list': exam_list
    }
    return render(request, "exams/exam.html", context)


# ===== Edit Exam =====
def edit_exam(request, slug):
    exam = get_object_or_404(Exam, slug=slug)
    subjects = Subject.objects.all()

    if request.method == "POST":
        exam.exam_name = request.POST.get('exam_name')
        subject_id = request.POST.get('subject')
        exam.subject = get_object_or_404(Subject, id=subject_id)

        exam.fees = request.POST.get('fees')
        exam.start_time = request.POST.get('start_time')
        exam.end_time = request.POST.get('end_time')
        exam.event_date = request.POST.get('event_date')

        exam.save()
        return redirect("exam_list")

    return render(request, "exams/edit-exam.html", {
        'exam': exam,
        'subjects': subjects
    })


# ===== View Exam =====
def view_exam(request, slug):
    exam = get_object_or_404(Exam, slug=slug)
    context = {
        'exam': exam
    }
    return render(request, "exams/exam-details.html", context)


# ===== Delete Exam =====
def delete_exam(request, slug):
    if request.method == "POST":
        exam = get_object_or_404(Exam, slug=slug)
        exam.delete()
        return redirect('exam_list')

    return HttpResponseForbidden()
