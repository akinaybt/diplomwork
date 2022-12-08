from django.contrib import admin
from .models import CustomUser, UserProfile, Appointment


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ['patient', 'referred_doctor', 'referred_department']
