from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('national_code',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('national_code',)}),
    )

    list_display = ('username', 'email', 'national_code', 'is_active')
    list_filter = ('is_active',)
    list_editable = ['is_active']

admin.site.register(CustomUser ,CustomUserAdmin)