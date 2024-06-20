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
    type = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}({self.type}) \n- {self.location}\n- {self.status}"

    class Meta:
        ordering = ['name']


# class SensorData(models.Model):
#     '''
#     SensorData model for storing sensor data from the microcontroller
#     - sensor: ForeignKey to Sensor
#     - value: Value of the sensor data
#     - timestamp: Time of the sensor data
#     '''

#     sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
#     value = models.FloatField()
#     timestamp = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.sensor} - {self.value} - {self.timestamp}"

#     class Meta:
#         ordering = ['-timestamp']
