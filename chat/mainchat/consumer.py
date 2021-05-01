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
        datapoint = json.loads(text_data)
        val = datapoint["value"]

        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'value':val
            }
        )
    
    async def deprocessing(self,event):
        valother = event["value"]
        await self.send(text_data = json.dumps({"value":valother}))