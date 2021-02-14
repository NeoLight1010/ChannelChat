import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send connect message to group.
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'User has connected.',
            }
        )

    async def tester_message(self, event):
        tester = event["tester"]

        await self.send(text_data=json.dumps({
            'tester': tester,
        }))

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'chatMessage': message
        }))

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['chatMessage']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def disconnect(self, close_code):
        # Send disconnect message
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'User has disconnected'
            }
        )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
