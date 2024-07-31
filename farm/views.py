from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from farm.models import Farm, Room, Location
from .serializers import (FarmSerializer, LocationSerializer, RoomSerializer, CO2SensorSerializer, LightSensorSerializer,
                          SoilMoistureSensorSerializer, TemperatureHumiditySensorSerializer, SensorDataSerializer)

from django.contrib.auth import get_user_model

User = get_user_model()


class FarmCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the farm'),
                'location': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'latitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Latitude of the farm'),
                        'longitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Longitude of the farm')
                    }
                )
            }
        ),
        responses={status.HTTP_201_CREATED: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Farm ID'),
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the farm'),
                'location': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'latitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Latitude of the farm'),
                        'longitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Longitude of the farm')
                    }
                )
            },
        )
        },
        operation_description='Create a new farm'
    )
    def post(self, request):
        location = Location.objects.create(**request.data.pop('location'))
        farm = request.data
        farm['location'] = location.pk
        serializer = FarmSerializer(data=farm)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoomCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer

    @ swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the room'),
                'mushroom_variety': openapi.Schema(type=openapi.TYPE_STRING, description='Type of mushroom'),
                'no_of_bags': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of bags in the room'),
                'farm': openapi.Schema(type=openapi.TYPE_INTEGER, description='Farm ID')
            }
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Room ID'),
                    'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the room'),
                    'mushroom_variety': openapi.Schema(type=openapi.TYPE_STRING, description='Type of mushroom'),
                    'no_of_bags': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of bags in the room'),
                    'farm': openapi.Schema(type=openapi.TYPE_INTEGER, description='Farm ID')
                }
            )
        },
        operation_description='Create a new room'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
