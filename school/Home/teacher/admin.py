from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'teacher_id', 'gender',
        'date_of_birth', 'joining_date',
        'mobile', 'qualification', 'experience'
    )

    search_fields = (
        'name', 'teacher_id', 'email',
        'mobile', 'qualification'
    )

    list_filter = (
        'gender', 'joining_date', 'qualification'
    )

    readonly_fields = ('teacher_image',)  # optional

    prepopulated_fields = {"slug": ("name", "teacher_id")}
