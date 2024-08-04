import os
import sys
import time
import asyncio
import json
import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer
import logging

MQTT_BROKER = os.environ.get('MQTT_BROKER', 'localhost')
MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Starts an MQTT listener.'

    username = os.environ.get('MQTT_USERNAME', '')
    password = os.environ.get('MQTT_PASSWORD', '')

    def handle(self, *args, **options):
        self.run_mqtt_listener()

    def run_mqtt_listener(self):
        client = mqtt.Client(protocol=mqtt.MQTTv5)
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        retry_count = 0
        max_retries = 10

        while retry_count < max_retries:
            try:
                client.username_pw_set(
                    username=self.username, password=self.password)
                client.connect(MQTT_BROKER, MQTT_PORT, 60)
                logger.info("Connected to MQTT broker: Success")
                client.loop_forever()
                break  # Exit loop if connection is successful
            except Exception as e:
                logger.error(f"Error connecting to MQTT broker: {e}")
                retry_count += 1
                time.sleep(5)  # Retry after 5 seconds

        if retry_count == max_retries:
            logger.error(
                "Failed to connect to MQTT broker after multiple attempts")

    def on_connect(self, client, userdata, flags, reason_code, properties):
        logger.info(f"Connected with result code {reason_code}")
        client.subscribe("sensor/monitor")
        client.subscribe("actuator/monitor")

    def on_message(self, client, userdata, msg):
        logger.info(f"Received message: {msg.topic} {msg.payload}")
        try:
            payload = json.loads(msg.payload.decode())
            farm_name = payload.get('farm_name', 'default_farm')
            if msg.topic == "sensor/monitor":
                asyncio.run(self.send_group_message(
                    farm_name, payload, 'sensor_monitor'))
            elif msg.topic == "actuator/monitor":
                asyncio.run(self.send_group_message(
                    farm_name, payload, 'actuator_monitor'))
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON payload")

    async def send_group_message(self, group_name, message, message_type):
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            group_name, {
                'type': message_type,
                'message': message
            }
        )
