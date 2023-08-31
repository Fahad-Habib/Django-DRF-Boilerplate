"""Register all models of the users app."""

from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Customize User interface on admin panel."""

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_verified', 'is_staff', 'is_superuser')
