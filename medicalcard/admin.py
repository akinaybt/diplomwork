from django.contrib import admin
from .models import Card


@admin.register(Card)
class Card(admin.ModelAdmin):
    list_display = ['patient']
