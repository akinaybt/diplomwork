from django.contrib import admin
from .models import DoctorProfile, Schedule, DoctorUser


@admin.register(DoctorUser)
class DoctorUser(admin.ModelAdmin):
    list_display = ['user']


@admin.register(DoctorProfile)
class DoctorProfile(admin.ModelAdmin):
    list_display = ['id', 'user', 'department', 'experience']


@admin.register(Schedule)
class Schedule(admin.ModelAdmin):
    list_display = ['doctor', 'weekday', 'start_time', 'end_time']
