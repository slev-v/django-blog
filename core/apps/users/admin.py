from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "email",
        "username",
        "karma",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("karma",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("karma",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
