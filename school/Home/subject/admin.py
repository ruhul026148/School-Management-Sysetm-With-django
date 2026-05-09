from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'subject_name',
        'subject_id',
        'student_class',
    )

    search_fields = (
        'subject_name',
        'subject_id',
        'student_class',
    )

    list_filter = (
        'student_class',
    )

    prepopulated_fields = {"slug": ("subject_name", "subject_id")}