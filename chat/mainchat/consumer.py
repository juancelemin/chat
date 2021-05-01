from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('hola')
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self):
        #await self.disconnect()
        pass
        

    async def receive(self, text_data):
        print (text_data)
        pass