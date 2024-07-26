from django.db import models
from farm.models import Room


class Sensor(models.Model):
    SENSOR_TYPE = (
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('temp & humidity', 'Temperature & Humidity'),
        ('soil_moisture', 'Soil Moisture'),
        ('co2', 'CO2'),
        ('light', 'Light'),
    )
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPE)
    last_updated = models.DateTimeField(auto_now=True)
    unit = models.CharField(max_length=10)
    location = models.CharField(max_length=50)

    class Meta:
        ordering = ['-last_updated']
        abstract = True


class SensorData(models.Model):
    SENSOR_TYPE = (
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('soil_moisture', 'Soil Moisture'),
        ('co2', 'CO2'),
        ('light', 'Light'),
    )
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPE)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=['sensor_type', 'timestamp']),
        ]


class TemperatureHumiditySensor(Sensor):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='temperature_humidity_sensor')
    temperature = models.ManyToManyField(
        SensorData, blank=True, related_name='temperature_data')
    humidity = models.ManyToManyField(
        SensorData, blank=True, related_name='humidity_data')

    def __str__(self):
        return f"{self.sensor_type} - {self.location}"


class SoilMoistureSensor(Sensor):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='soil_moisture_sensor')
    moisture_level = models.ManyToManyField(
        SensorData, blank=True, related_name='moisture_data')

    def __str__(self):
        return f"{self.sensor_type} - {self.location}"


class CO2Sensor(Sensor):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='co2_sensor')
    co2_level = models.ManyToManyField(
        SensorData, blank=True, related_name='co2_data')

    def __str__(self):
        return f"{self.sensor_type} - {self.location}"


class LightSensor(Sensor):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='light_sensor')
    light_level = models.ManyToManyField(
        SensorData, blank=True, related_name='light_data')

    def __str__(self):
        return f"{self.sensor_type} - {self.location}"
