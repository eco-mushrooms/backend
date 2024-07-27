from rest_framework import serializers
from sensor.models import SensorData, TemperatureHumiditySensor, SoilMoistureSensor, CO2Sensor, LightSensor
from farm.models import Room, Farm, Location


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'


class TemperatureHumiditySensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureHumiditySensor
        fields = '__all__'


class SoilMoistureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilMoistureSensor
        fields = '__all__'


class CO2SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CO2Sensor
        fields = '__all__'


class LightSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightSensor
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'
