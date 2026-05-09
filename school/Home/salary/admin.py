from django.contrib import admin
from .models import Salary


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    # List view
    list_display = (
        'staff_id',
        'name',
        'gender',
        'joining_date',
        'amount',
        'created_at',
    )

    # Filter sidebar
    list_filter = (
        'gender',
        'joining_date',
        'created_at',
    )

    # Search
    search_fields = (
        'staff_id',
        'name',
    )

    # Auto slug
    prepopulated_fields = {'slug': ('staff_id', 'name')}

    # Ordering
    ordering = ('-created_at',)

    # Readonly
    readonly_fields = ('created_at',)

    # Pagination
    list_per_page = 20

    # Field grouping (clean UI)
    fieldsets = (
        ('Basic Info', {
            'fields': ('staff_id', 'name')
        }),
        ('Personal Info', {
            'fields': ('gender', 'joining_date')
        }),
        ('Salary Info', {
            'fields': ('amount',)
        }),
        ('Extra', {
            'fields': ('slug', 'created_at')
        }),
    )