from django.contrib import admin
from .models import CustomUser
# Register your models here.

# admin.site.register(CustomUser)




@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    'is_author',
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )