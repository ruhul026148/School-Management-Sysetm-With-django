from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Expenses


# ===== Add Expenses =====
def add_expenses(request):
    if request.method == "POST":
        expenses_id = request.POST.get('expenses_id')
        item_name = request.POST.get('item_name')
        item_quality = request.POST.get('item_quality')
        expense_amount = request.POST.get('expense_amount')
        source_of_purchase = request.POST.get('source_of_purchase')

        Expenses.objects.create(
            expenses_id=expenses_id,
            item_name=item_name,
            item_quality=item_quality,
            expense_amount=expense_amount,
            source_of_purchase=source_of_purchase
        )

        messages.success(request, "Expense added successfully")
        return redirect("expenses_list")

    return render(request, "expenses/add-expenses.html")


# ===== Expenses List =====
def expenses_list(request):
    expenses_list = Expenses.objects.all().order_by('-created_at')

    context = {
        'expenses_list': expenses_list
    }

    return render(request, "expenses/expenses.html", context)