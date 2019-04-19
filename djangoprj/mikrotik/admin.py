from django.contrib import admin
from .models import MTActivity, MTLogin, MTUsers, MTSession, MTSnapshot
# Register your models here.


class MTSessionAdmin(admin.ModelAdmin):
    list_display = ['ip', 'host_name', 'mac']
    search_fields = ['ip']

admin.site.register(MTSession,MTSessionAdmin) 


class MTLoginAdmin(admin.ModelAdmin):
    list_display = ['mac', 'ip', 'time']
    search_fields = ['ip']

admin.site.register(MTLogin, MTLoginAdmin) 


class MTSnapshotAdmin(admin.ModelAdmin):
    list_display = ['mac', 'ip', 'activity', 'time']
    search_fields = ['ip', 'mac']

admin.site.register(MTSnapshot, MTSnapshotAdmin) 


class MTActivityAdmin(admin.ModelAdmin):
    list_display = ['bytes', 'ip', 'time', 'log_records']
    search_fields = ['ip']

admin.site.register(MTActivity, MTActivityAdmin)

class MTUsersAdmin(admin.ModelAdmin):
    list_display = ['ip', 'mac', 'host']
    search_fields = ['ip']

admin.site.register(MTUsers, MTUsersAdmin)
