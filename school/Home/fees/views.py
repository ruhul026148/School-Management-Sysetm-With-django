from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Fees
from django.contrib import messages


# ===== Add Fees =====
def add_fees(request):
    if request.method == "POST":
        fees_id = request.POST.get('fees_id')
        fees_type = request.POST.get('fees_type')
        student_class = request.POST.get('student_class')
        fees_amount = request.POST.get('fees_amount')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        Fees.objects.create(
            fees_id=fees_id,
            fees_type=fees_type,
            student_class=student_class,
            fees_amount=fees_amount,
            start_date=start_date,
            end_date=end_date
        )

        messages.success(request, "Fees added successfully")
        return redirect("fees_list")

    return render(request, "fees/add-fees.html")


# ===== Fees List =====
def fees_list(request):
    fees_list = Fees.objects.all().order_by('-start_date')
    context = {
        'fees_list': fees_list
    }
    return render(request, "fees/fees.html", context)


# ===== Edit Fees =====
def edit_fees(request, slug):
    fees = get_object_or_404(Fees, slug=slug)

    if request.method == "POST":
        fees.fees_id = request.POST.get('fees_id')
        fees.fees_type = request.POST.get('fees_type')
        fees.student_class = request.POST.get('student_class')
        fees.fees_amount = request.POST.get('fees_amount')
        fees.start_date = request.POST.get('start_date')
        fees.end_date = request.POST.get('end_date')

        fees.save()
        return redirect("fees_list")

    return render(request, "fees/edit-fees.html", {
        'fees': fees
    })


# ===== View Fees =====
def view_fees(request, slug):
    fees = get_object_or_404(Fees, slug=slug)
    context = {
        'fees': fees
    }
    return render(request, "fees/fees-details.html", context)


# ===== Delete Fees =====
def delete_fees(request, slug):
    if request.method == "POST":
        fees = get_object_or_404(Fees, slug=slug)
        fees.delete()
        return redirect('fees_list')

    return HttpResponseForbidden()