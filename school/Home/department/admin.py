from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'department_name',
        'department_id',
        'head_of_department',
        'department_start_date',
        'no_of_students',
    )

    search_fields = (
        'department_name',
        'department_id',
        'head_of_department',
    )

    list_filter = (
        'department_start_date',
    )

    ordering = ('department_name',)

    prepopulated_fields = {"slug": ("department_name", "department_id")}