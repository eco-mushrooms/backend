from django.db import models


class Microcontroller(models.Model):
    '''
    Microcontroller model
    - name: Name of the microcontroller
    - type: Type of the microcontroller e.g Arduino, ESP32
    - location: Location of the microcontroller
    - connected_senores: List[Sensor] of connected sensors
    - status: Operational status of the microcontroller
    '''

    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    location = models.CharField(max_length=50)
    model_make = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}({self.model_make}) \n- {self.location}\n- {self.status}"

    class Meta:
        ordering = ['name']
