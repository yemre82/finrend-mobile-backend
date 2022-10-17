from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from django.db.models import Q

from users.models import CustomUser
from messages.models import Message


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages_usernames(request):
    user = request.user
    message_obj = Message.objects.filter(Q(sender=user) | Q(receiver=user)).order_by("-created_at")
    returning_list = []
    for message in message_obj:
        if message.sender == user:
            if message.receiver.username not in returning_list["username"]:
                return_obj={
                    "is_sender":False,
                    "username":message.receiver.username,
                    "message":message.message,
                    "is_read":message.is_read,
                    "image":"/media/"+str(message.image),
                    "created_at":message.created_at,
                }
                returning_list.append(return_obj)
        else:
            if message.sender.username not in returning_list["username"]:
                return_obj={
                    "is_sender":True,
                    "username":message.sender.username,
                    "message":message.message,
                    "is_read":message.is_read,
                    "image":"/media/"+str(message.image),
                    "created_at":message.created_at,
                }
                returning_list.append(return_obj)
    return response_200(returning_list)