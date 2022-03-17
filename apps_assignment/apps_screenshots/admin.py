from django.contrib import admin
from .models import Apps,Screenshots
from django import forms

class AppsAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at', 'updated_at')

class ScreenshotsAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at', 'updated_at')


admin.site.register(Apps, AppsAdmin)
admin.site.register(Screenshots, ScreenshotsAdmin)