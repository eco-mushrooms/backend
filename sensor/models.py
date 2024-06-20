from django.db import models


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
    microcontroller = models.ForeignKey(
        'mushroom.Microcontroller', on_delete=models.CASCADE)
    unit = models.CharField(max_length=10)
    location = models.CharField(max_length=50)

    class Meta:
        ordering = ['-last_updated']
        abstract = True


class TemperatureHumiditySensor(Sensor):
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"{self.sensor_type} - {self.temperature}C - {self.humidity}% - {self.location}"


class SoilMoistureSensor(Sensor):
    moisture_level = models.FloatField()

    def __str__(self):
        return f"{self.sensor_type} - {self.moisture_level} {self.unit} - {self.location}"


class CO2Sensor(Sensor):
    co2_level = models.FloatField()

    def __str__(self):
        return f"{self.sensor_type} - {self.co2_level} ppm - {self.location}"


class LightSensor(Sensor):
    light_level = models.FloatField()

    def __str__(self):
        return f"{self.sensor_type} - {self.light_level} lux - {self.location}"
