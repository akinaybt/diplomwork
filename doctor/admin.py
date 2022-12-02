from django.contrib import admin
from .models import DoctorProfile, Schedule, DoctorUser

admin.site.register(Schedule)
admin.site.register(DoctorUser)


@admin.register(DoctorProfile)
class DoctorProfile(admin.ModelAdmin):
    list_display = ['id', 'user', 'department', 'experience']

