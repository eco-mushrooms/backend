from django.db import models
from microcontroller.models import Microcontroller


class Location(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return f'Lat: {self.latitude}\nLong: {self.longitude}'


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    mushroom_variety = models.CharField(max_length=100)
    microcontroller = models.ForeignKey(
        Microcontroller, related_name='microcontroller', on_delete=models.SET_NULL, null=True)
    no_of_bags = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} - {self.mushroom_variety}'


class Farm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True)
    rooms = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.name} at\n{self.location}'
