from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json


class MushroomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['farm_name']

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        # Send a message to the client when a new connection is established
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'new_connection',
                'message': 'New connection established'
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):  # ignore the warning, it's a false positive
        text_data = json.loads(text_data)
        print(text_data)
        message = text_data['message']
        _type = text_data['type']

        if _type == 'monitor':
            room = text_data['room']
            sensor_data: dict = text_data['sensor_data']

            # TODO: Save sensor data to the database (I advice we dedicate a background task to do this i.e using
            #   celery)
            # For now lets relay the data first to the channel layer
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'monitor',
                    'room': room,
                    'message': message,
                    'sensor_data': sensor_data
                }
            )

    async def monitor(self, event):
        microcontroller_name = event['microcontroller_name']
        sensor_data = event['sensor_data']
        await self.send(text_data=json.dumps({
            'microcontroller_name': microcontroller_name,
            'sensor_data': sensor_data
        }))

    async def new_connection(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def error_message(self, error_message: str):
        await self.send(text_data=json.dumps({'error': error_message}))
