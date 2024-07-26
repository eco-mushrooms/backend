from django.urls import path
from .consumer import MushroomConsumer

websocket_urlpatterns = [
    path('ws/mushroom/<str:farm_name>/', MushroomConsumer.as_asgi()),
]
