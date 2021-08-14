# apps/users/admin.py

# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Locals
from apps.users.models import MyCustomUser

# Register your models here.

@admin.register(MyCustomUser) # <-- it equal to '@admin.register(models.MyCustomUser)'
# class MyCustomUserAdmin(admin.ModelAdmin):

#     """ Custom User Admin """

#     list_display = ("username", "email", "gender", "language", "currency", "superhost")
#     list_filter = ("language", "currency", "superhost")

class MyCustomUserAdmin(UserAdmin):

    """ Custom User Admin """
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
