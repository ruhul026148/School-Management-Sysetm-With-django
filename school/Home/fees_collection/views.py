from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden

from .models import FeesCollection
from student.models import Student


# ===== Add Fees =====
def add_fees(request):
    students = Student.objects.all()

    if request.method == "POST":
        student_id = request.POST.get('student')
        fees_type = request.POST.get('fees_type')
        fees_amount = request.POST.get('fees_amount')
        paid_date = request.POST.get('paid_date')

        student = get_object_or_404(Student, id=student_id)

        FeesCollection.objects.create(
            student=student,
            fees_type=fees_type,
            fees_amount=fees_amount,
            paid_date=paid_date
        )

        messages.success(request, "Fees added successfully")
        return redirect("fees_collection_list")

    return render(request, "fees_collections/add-fees-collection.html", {
        'students': students
    })


# ===== Fees List =====
def fees_collection_list(request):
    fees_collection_list = FeesCollection.objects.select_related('student').all()

    context = {
        'fees_collection_list': fees_collection_list
    }

    return render(request, "fees_collections/fees-collections.html", context)


# ===== View Fees =====
