import os
import json
import paho.mqtt.client as mqtt
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.management.base import BaseCommand


MQTT_BROKER = f'mqtt://{os.environ.get("MQTT_BROKER")}'
MQTT_PORT = 1883
MQTT_TOPIC = 'sensor/data'


class Command(BaseCommand):
    help = 'MQTT consumer'

    def handle(self, *args, **options):
        def on_connect(client, userdata, flags, rc):
            print('Connected with result code ' + str(rc))
            client.subscribe(MQTT_TOPIC)

        def on_message(client, userdata, msg):
            payload = json.loads(msg.payload)
            print('Received message: ' + str(payload))

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'sensor_data',
                {
                    'type': 'sensor_data',
                    'payload': payload
                }
            )

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_forever()
