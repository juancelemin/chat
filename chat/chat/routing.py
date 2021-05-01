# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from mainchat import consumer
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat.settings")


websocket_urlPattern = [
    path('ws/polData/',consumer.ChatConsumer.as_asgi())
]
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlPattern
        )
    ),
})
