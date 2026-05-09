from django.contrib import admin
from .models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'exam_name',
        'subject',
        'get_class',
        'fees',
        'event_date',
        'start_time',
        'end_time',
    )

    search_fields = (
        'exam_name',
        'subject__subject_name',
        'subject__subject_id',
    )

    list_filter = (
        'event_date',
        'subject__student_class',
    )

    ordering = ('event_date', 'start_time')

    prepopulated_fields = {"slug": ("exam_name",)}

    # 🔥 Custom column for class (from Subject)
    def get_class(self, obj):
        return obj.subject.student_class
    get_class.short_description = "Class"
