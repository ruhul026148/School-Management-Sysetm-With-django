from django.contrib import admin
from .models import FeesCollection


@admin.register(FeesCollection)
class FeesCollectionAdmin(admin.ModelAdmin):

    list_display = (
        'get_student_id',
        'get_student_name',
        'get_student_class',
        'get_student_section',
        'fees_type',
        'fees_amount',
        'paid_date',
    )

    list_filter = ('fees_type', 'paid_date', 'student__student_class')

    search_fields = (
        'student__student_id',
        'student__first_name',
        'student__last_name',
    )

    # 👉 Custom functions to show student data
    def get_student_id(self, obj):
        return obj.student.student_id
    get_student_id.short_description = 'Student ID'

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"
    get_student_name.short_description = 'Student Name'

    def get_student_class(self, obj):
        return obj.student.student_class
    get_student_class.short_description = 'Class'

    def get_student_section(self, obj):
        return obj.student.section
    get_student_section.short_description = 'Section'