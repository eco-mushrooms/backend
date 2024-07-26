from rest_framework import serializers
from sensor.models import SensorData, TemperatureHumiditySensor, SoilMoistureSensor, CO2Sensor, LightSensor
from farm.models import Room, Farm, Location
