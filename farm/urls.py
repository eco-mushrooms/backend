from django.urls import path

from .views import FarmCreateView, RoomCreateView

urlpatterns = [
    path('create', FarmCreateView.as_view(), name='farm-create'),
    path('room/create', RoomCreateView.as_view(), name='room-create'),
]
