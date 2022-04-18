from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from .models import Reservation

@register(Reservation)
class ReservationAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'number_of_number', 'Date', 'time',)