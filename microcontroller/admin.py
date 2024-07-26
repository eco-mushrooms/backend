from django.contrib import admin
from .models import Microcontroller


@admin.register(Microcontroller)
class MicrocontrollerAdmin(admin.ModelAdmin):
    list_display = ('name', 'model_make', 'location', 'status')
    list_filter = ('location', 'status')
    search_fields = ('name', 'location')
    ordering = ('name',)
