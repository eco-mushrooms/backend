from django.contrib import admin
from .models import (
    TemperatureHumiditySensor,
    SoilMoistureSensor,
    CO2Sensor,
    LightSensor
)


@admin.register(TemperatureHumiditySensor)
class TemperatureHumiditySensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'temperature',
                    'humidity', 'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('location',)
    ordering = ('-last_updated',)


@admin.register(SoilMoistureSensor)
class SoilMoistureSensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'moisture_level',
                    'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('location', )
    ordering = ('-last_updated',)


@admin.register(CO2Sensor)
class CO2SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'co2_level', 'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('location',)
    ordering = ('-last_updated',)


@admin.register(LightSensor)
class LightSensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'light_level', 'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('location',)
    ordering = ('-last_updated',)
