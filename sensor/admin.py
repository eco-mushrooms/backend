from django.contrib import admin
from .models import (
    CO2Sensor,
    SensorData,
    LightSensor,
    SoilMoistureSensor,
    TemperatureHumiditySensor,
)


@admin.register(TemperatureHumiditySensor)
class TemperatureHumiditySensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('location',)
    ordering = ('-last_updated',)


@admin.register(SoilMoistureSensor)
class SoilMoistureSensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('location', )
    ordering = ('-last_updated',)


@admin.register(CO2Sensor)
class CO2SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('location',)
    ordering = ('-last_updated',)


@admin.register(LightSensor)
class LightSensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('location',)
    ordering = ('-last_updated',)


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'timestamp', 'value')
    list_filter = ('sensor_type', 'timestamp')
    search_fields = ('sensor_type', 'timestamp')
    ordering = ('-timestamp',)
