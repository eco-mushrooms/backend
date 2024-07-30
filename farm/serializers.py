import logging
from rest_framework import serializers
from farm.models import Room, Farm, Location
from sensor.models import SensorData, TemperatureHumiditySensor, SoilMoistureSensor, CO2Sensor, LightSensor

logger = logging.getLogger('farm.serializers')


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


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

    # def validate(self, attrs):
    #     location_data = attrs.pop('location')

    #     if location is None:
    #         raise serializers.ValidationError("Location is required")

    #     location = Location.objects.create(**location_data)

    #     logger.debug(f'Location created: {location}')

    #     attrs['location'] = location.pk

    #     logger.debug(f'Farm attrs: {attrs}')

    #     return attrs
