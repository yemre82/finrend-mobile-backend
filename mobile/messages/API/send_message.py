from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from users.models import CustomUser
from messages.models import Message


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    sender = request.user
    receiver_username = request.data.get("receiver_username")
    message = request.data.get("message")
    image = request.data.get("image")
    try:
        receiver_obj = CustomUser.objects.get(username=receiver_username)
    except ObjectDoesNotExist as e:
        return response_400("There is no such User")
    if message == None and image == None:
        return response_400("Please send a message or image")
    Message.objects.create(
        sender=sender, receiver=receiver_obj, message=message, image=image)
    return response_200(None)