from django.contrib import admin
from .models import CustomUser, PasswordResetRequest


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_authorized', 'is_staff', 'is_superuser')
    list_filter = ('is_authorized', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('-id',)


@admin.register(PasswordResetRequest)
class PasswordResetRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'token', 'created_at', 'is_valid_display')
    search_fields = ('user__email', 'token')
    ordering = ('-created_at',)

    def is_valid_display(self, obj):
        return obj.is_valid()
    
    is_valid_display.boolean = True
    is_valid_display.short_description = 'Is Valid'