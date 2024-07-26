from django.contrib import admin
from .models import Room, Farm, Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude')
    search_fields = ('latitude', 'longitude')
    ordering = ('latitude',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'mushroom_variety',
                    'microcontroller', 'no_of_bags')
    list_filter = ('mushroom_variety', 'microcontroller')
    search_fields = ('name', 'mushroom_variety')
    ordering = ('name',)


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ('location',)
    search_fields = ('name', 'location')
    ordering = ('name',)
