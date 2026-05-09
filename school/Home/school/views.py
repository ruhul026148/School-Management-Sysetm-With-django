from django.http import HttpResponse
from django.shortcuts import render

from student.models import Student
from teacher.models import Teacher
from department.models import Department
from subject.models import Subject

# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

def admin_dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_department=Department.objects.count()
    total_subjects = Subject.objects.count()
    total_classes = Student.objects.values('student_class').distinct().count()
    
    context = {
        'total_students': total_students,
        'total_teachers':total_teachers,
        'total_department':total_department,
        'total_subjects':total_subjects,
        'total_classes':total_classes,
    }
    return render(request, "Home/index.html",context)

def dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_department=Department.objects.count()
    total_subjects = Subject.objects.count()
    total_classes = Student.objects.values('student_class').distinct().count()
    
    context = {
        'total_students': total_students,
        'total_teachers':total_teachers,
        'total_department':total_department,
        'total_subjects':total_subjects,
        'total_classes':total_classes,
    }
    return render(request, "Home/index.html",context)