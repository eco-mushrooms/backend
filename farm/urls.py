from django.urls import path

from .views import FarmCreateView

urlpatterns = [
    path('create', FarmCreateView.as_view(), name='farm-create'),
]
