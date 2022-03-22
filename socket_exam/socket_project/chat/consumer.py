import json
from channels.generic.websocket import AsyncWebsocketConsumer

# from django.contrib.sessions.backends.db import SessionStore

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user = self.scope['user']
        self.room_group_name = 'chat_%s' % self.room_name
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notice',
                'sender' : {
                    'message': f"{self.user}님이 들어왔습니다.",
                    'send' : str(self.user)
                }
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notice',
                'sender' : {
                    'message': f"{self.user}님이 나갔습니다.",
                    'send' : str(self.user)
                }
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender' : {
                    "username" : str(self.user),
                    "message" : message
                }
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['sender']['message']
        me = str(self.user)
        send = event['sender']['username']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'me' : me,
            'send' : send,
            'notice' : False
        }))

    async def notice(self, event):
        message = event['sender']['message']
        me = event['sender']['send']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'me' : me,
            'send' : me,
            'notice' : True
        }))

