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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_message(request):
    receiver=request.user
    sender_username=request.data.get("sender_username")
    try:
        sender_obj=CustomUser.objects.get(username=sender_username)
    except ObjectDoesNotExist as e:
        return response_400("There is no such User")
    message_obj=Message.objects.filter(Q(sender=sender_obj,receiver=receiver)|Q(sender=receiver,receiver=sender_obj)).order_by("-created_at")
    returning_list=[]
    for message in message_obj:
        if message.sender==sender_obj:
            return_obj={
                "is_sender":True,
                "message":message.message,
                "is_read":message.is_read,
                "image":"/media/"+str(message.image),
                "created_at":message.created_at,
            }
            returning_list.append(return_obj)
        else:
            return_obj={
                "is_sender":False,
                "message":message.message,
                "is_read":message.is_read,
                "image":"/media/"+str(message.image),
                "created_at":message.created_at,
            }
            returning_list.append(return_obj)
            message.is_read=True
            message.save()
    return response_200(returning_list)