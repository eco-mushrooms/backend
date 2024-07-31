from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Location(models.Model):
    latitude = models.DecimalField(max_digits=13, decimal_places=9)
    longitude = models.DecimalField(max_digits=13, decimal_places=9)

    def __str__(self):
        return f'Lat: {self.latitude}\nLong: {self.longitude}'


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    mushroom_variety = models.CharField(max_length=100)
    no_of_bags = models.IntegerField()
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Farm: {self.farm}\nRoom: {self.name}\nMushroom Variety: {self.mushroom_variety}\nMicrocontroller: {self.microcontroller}\nNo of Bags: {self.no_of_bags}'


class Farm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.name} at\n{self.location}'
