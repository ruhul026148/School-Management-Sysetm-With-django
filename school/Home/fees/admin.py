from django.contrib import admin
from .models import Fees


@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = (
        'fees_id',
        'fees_type',
        'student_class',
        'fees_amount',
        'start_date',
        'end_date'
    )

    list_filter = (
        'fees_type',
        'student_class',
        'start_date',
    )

    search_fields = (
        'fees_id',
        'student_class',
    )

    prepopulated_fields = {'slug': ('fees_id',)}

    ordering = ('start_date',)
