from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'role', 'is_active', 'is_staff']
    search_fields = ['email', 'username']
    list_filter = ['role', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'role', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(Profile)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'farm']
    search_fields = ['user__email']
    list_filter = ['farm']
    fieldsets = (
        (None, {'fields': ('user', 'farm')}),
    )
    ordering = ['user']
    filter_horizontal = ()
