from django.contrib import admin

# Register your models here.

from .models import WUsers, WTasks

class WTaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_to', 'user_from']
    search_fields = ['user_to']

admin.site.register(WTasks, WTaskAdmin)


class WUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['email', 'name']

admin.site.register(WUsers, WUserAdmin)

