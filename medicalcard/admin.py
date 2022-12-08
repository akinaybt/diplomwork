from django.contrib import admin
from .models import Card, MakeAppointment


@admin.register(Card)
class Card(admin.ModelAdmin):
    list_display = ['patient']


@admin.register(MakeAppointment)
class MakeAppointment(admin.ModelAdmin):
    list_display = ['id']
