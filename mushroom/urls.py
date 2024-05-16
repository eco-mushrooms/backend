from django.urls import path
from .views import MushroomView
from .consumer import MushroomConsumer


urlpatterns = [
    path('', MushroomView.as_view(), name='mushroom'),
]

websocket_urlpatterns = [
    path('ws/mushroom/', MushroomConsumer.as_asgi()),
]
