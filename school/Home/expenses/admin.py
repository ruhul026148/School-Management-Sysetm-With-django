from django.contrib import admin
from .models import Expenses


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    # List view (table এ কি কি দেখাবে)
    list_display = (
        'expenses_id',
        'item_name',
        'item_quality',
        'expense_amount',
        'source_of_purchase',
        'created_at',
    )

    # Sidebar filter
    list_filter = (
        'item_quality',
        'created_at',
    )

    # Search bar
    search_fields = (
        'expenses_id',
        'item_name',
        'source_of_purchase',
    )

    # Slug auto fill
    prepopulated_fields = {'slug': ('expenses_id', 'item_name')}

    # Ordering
    ordering = ('-created_at',)

    # Readonly field (optional)
    readonly_fields = ('created_at',)

    # Pagination (optional)
    list_per_page = 20
