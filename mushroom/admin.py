from django.contrib import admin
from .models import Microcontroller


@admin.register(Microcontroller)
class MicrocontrollerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location', 'status')
    list_filter = ('location', 'status')
    search_fields = ('name', 'location')
    ordering = ('name',)


# @admin.register(SensorData)
# class SensorDataAdmin(admin.ModelAdmin):
#     list_display = ('sensor', 'value', 'timestamp')
#     list_filter = ('sensor', 'timestamp')
#     search_fields = ('sensor', 'timestamp')
#     ordering = ('-timestamp',)
