from django.urls import path
from .views import MushroomView


urlpatterns = [
    path('', MushroomView.as_view(), name='mushroom'),
]
