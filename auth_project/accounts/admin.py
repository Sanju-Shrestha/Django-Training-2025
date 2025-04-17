from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_banned')
    list_filter = ('is_staff', 'is_superuser', 'is_banned')
    actions = ['ban_users', 'unban_users']

    def ban_users(self, request, queryset):
        queryset.update(is_banned=True)
    ban_users.short_description = "Ban selected users"

    def unban_users(self, request, queryset):
        queryset.update(is_banned=False)
    unban_users.short_description = "Unban selected users"

admin.site.register(CustomUser, CustomUserAdmin)