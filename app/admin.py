from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the admin list view
    list_display = ('name', 'email', 'password')


admin.site.register(CustomUser, CustomUserAdmin)
