import os
import sys
import time
import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

MQTT_BROKER = os.environ.get('MQTT_BROKER', 'localhost')
MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))


class ReloadHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command

    def on_any_event(self, event):
        if event.event_type in ('modified', 'created', 'deleted'):
            print("Change detected. Reloading...")
            self.command.should_reload = True


class Command(BaseCommand):
    help = 'Starts an MQTT listener with autoreload functionality.'

    def handle(self, *args, **options):
        self.should_reload = False

        event_handler = ReloadHandler(self)
        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=True)
        observer.start()

        try:
            while True:
                if self.should_reload:
                    self.reload()
                    self.should_reload = False
                self.run_mqtt_listener()
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def reload(self):
        print("Reloading...")
        os.execv(sys.executable, ['python'] + sys.argv)

    def run_mqtt_listener(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            client.loop_start()
        except Exception as e:
            print(f"Error connecting to MQTT broker: {e}")
            time.sleep(5)  # Retry after 5 seconds

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        client.subscribe("your/topic")

    def on_message(self, client, userdata, msg):
        print(f"{msg.topic} {msg.payload}")
