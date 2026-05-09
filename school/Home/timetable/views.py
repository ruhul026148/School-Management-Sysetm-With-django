from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import TimeTable
from django.contrib import messages


# ===== Add TimeTable =====
def add_timetable(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        name = request.POST.get('name')
        student_class = request.POST.get('student_class')
        section = request.POST.get('section')
        subject = request.POST.get('subject')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        TimeTable.objects.create(
            teacher_id=teacher_id,
            name=name,
            student_class=student_class,
            section=section,
            subject=subject,
            date=date,
            start_time=start_time,
            end_time=end_time
        )

        messages.success(request, "Time Table added successfully")
        return redirect("timetable_list")

    return render(request, "timetables/add-time-table.html")


# ===== TimeTable List =====
def timetable_list(request):
    timetable_list = TimeTable.objects.all()
    context = {
        'timetable_list': timetable_list
    }
    return render(request, "timetables/time-table.html", context)


# ===== Edit TimeTable =====
def edit_timetable(request, slug):
    timetable = get_object_or_404(TimeTable, slug=slug)

    if request.method == "POST":
        timetable.teacher_id = request.POST.get('teacher_id')
        timetable.name = request.POST.get('name')
        timetable.student_class = request.POST.get('student_class')
        timetable.section = request.POST.get('section')
        timetable.subject = request.POST.get('subject')
        timetable.date = request.POST.get('date')
        timetable.start_time = request.POST.get('start_time')
        timetable.end_time = request.POST.get('end_time')

        timetable.save()
        return redirect("timetable_list")

    return render(request, "timetables/edit-time-table.html", {'timetable': timetable})


# ===== View TimeTable =====
def view_timetable(request, slug):
    timetable = get_object_or_404(TimeTable, slug=slug)
    context = {
        'timetable': timetable
    }
    return render(request, "timetable/timetable-details.html", context)


# ===== Delete TimeTable =====
def delete_timetable(request, slug):
    if request.method == "POST":
        timetable = get_object_or_404(TimeTable, slug=slug)
        timetable.delete()
        return redirect('timetable_list')

    return HttpResponseForbidden()