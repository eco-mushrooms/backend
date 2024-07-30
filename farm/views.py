from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from farm.models import Farm, Room, Location
from .serializers import (FarmSerializer, LocationSerializer, RoomSerializer, CO2SensorSerializer, LightSensorSerializer,
                          SoilMoistureSensorSerializer, TemperatureHumiditySensorSerializer, SensorDataSerializer)

from django.contrib.auth import get_user_model

User = get_user_model()


class FarmCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=FarmSerializer,
        responses={status.HTTP_201_CREATED: FarmSerializer},
        operation_description='Create a new farm'
    )
    def post(self, request):
        location = Location.objects.create(**request.data.pop('location'))
        farm = request.data
        farm['location'] = location.pk
        serializer = FarmSerializer(data=farm)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoomCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        room = request.data
        serializer = RoomSerializer(data=room)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
