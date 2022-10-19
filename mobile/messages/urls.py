from django.urls import path
from messages.API.get_message import get_message

from messages.API.get_messages_usernames import get_messages_usernames
from messages.API.send_message import send_message

urlpatterns = [
    path("get_messages_usernames", get_messages_usernames),
    path("get-message",get_message),
    path("send-message",send_message),
]