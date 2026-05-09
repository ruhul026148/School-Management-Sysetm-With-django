from django.contrib import admin
from .models import TimeTable


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = (
        'teacher_id',
        'name',
        'student_class',
        'section',
        'subject',
        'date',
        'start_time',
        'end_time',
    )

    search_fields = (
        'teacher_id',
        'name',
        'subject',
        'student_class',
    )

    list_filter = (
        'date',
        'student_class',
        'section',
    )

    ordering = ('date', 'start_time')

    prepopulated_fields = {"slug": ("teacher_id", "subject", "date")}