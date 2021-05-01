from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    datapoint =[]
    users = []
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
        
        self.datapoint.append(json.loads(text_data))
        
        (json.loads(text_data)["user"]) if  not (json.loads(text_data)["user"]) in self.users else ''

        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'value':self.datapoint,
                'users':self.users,
            }
        )
    
    async def deprocessing(self,event):
        valother = event
        await self.send(text_data = json.dumps(valother))