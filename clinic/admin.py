from django.contrib import admin

from .models import Clinic, Department


@admin.register(Clinic)
class Clinic(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = ['title']
