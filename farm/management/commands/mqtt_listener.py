import os
import sys
import time
import logging
import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer

logger = logging.getLogger(__name__)
MQTT_BROKER = os.environ.get('MQTT_BROKER', 'localhost')
MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))
MAX_RETRIES = 10
RETRY_INTERVAL = 5  # seconds


class Command(BaseCommand):
    help = 'Starts an MQTT listener.'

    username = os.environ.get('MQTT_USERNAME', '')
    password = os.environ.get('MQTT_PASSWORD', '')

    def handle(self, *args, **options):
        self.run_mqtt_listener()

    def run_mqtt_listener(self):
        failure_count = 0

        while failure_count < MAX_RETRIES:
            client = mqtt.Client(protocol=mqtt.MQTTv5)
            client.on_connect = self.on_connect
            client.on_message = self.on_message

            try:
                client.username_pw_set(
                    username=self.username, password=self.password)
                client.connect(MQTT_BROKER, MQTT_PORT, 60)
                client.loop_forever()
                break  # Exit loop if connection is successful
            except Exception as e:
                logger.error(f"Error connecting to MQTT broker: {e}")
                failure_count += 1
                if failure_count < MAX_RETRIES:
                    logger.info(
                        f"Retrying in {RETRY_INTERVAL} seconds ({failure_count}/{MAX_RETRIES})...")
                    time.sleep(RETRY_INTERVAL)
                else:
                    logger.error(
                        f"Max retries reached ({MAX_RETRIES}). Exiting....")
                    # Exit with an error code if max retries reached
                    sys.exit(1)

    def on_connect(self, client, userdata, flags, reason_code, properties):
        logger.info(f"Connected to MQTT broker: {reason_code}")
        client.subscribe("sensor/monitor")
        client.subscribe("actuator/monitor")

    def on_message(self, client, userdata, msg):
        logger.info(f"Received message: {msg.topic} {msg.payload.decode()}")
        if msg.topic == "sensor/monitor":
            channel_layer = get_channel_layer()
            channel_layer.group_send(
                'sensor_monitor', {
                    'type': 'sensor_monitor',
                    'message': msg.payload.decode()
                }
            )
        elif msg.topic == "actuator/monitor":
            channel_layer = get_channel_layer()
            channel_layer.group_send(
                'actuator_monitor', {
                    'type': 'actuator_monitor',
                    'message': msg.payload.decode()
                }
            )
