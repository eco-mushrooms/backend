from celery import shared_task
from channels.layers import get_channel_layer


@shared_task(bind=True, name='tasks.save_sensor_data')
def save_sensor_data(self, microcontroller_name: str, sensor_data: dict):
    print('Saving sensor data')
    sensor_data = {
        'microcontroller': microcontroller_name,
        'sensor_data': sensor_data
    }

    print(sensor_data)
    print('Sensor data saved')
