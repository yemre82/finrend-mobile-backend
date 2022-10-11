from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from users.models import CustomUser


@api_view(['POST'])
@permission_classes([AllowAny])
def new_password_email(request):
    email=request.data.get("email")
    try:
        user_obj=CustomUser.objects.get(email=email)
    except ObjectDoesNotExist as e:
        return response_400("There is no such Email")
    password = request.data.get("password")
    if len(password) < 8:
        return response_400("Please send a valid Password (at least 8 digit)")
    user_obj.set_password(password)
    user_obj.save()
    return response_200(None)


@api_view(['POST'])
@permission_classes([AllowAny])
def new_password_phone(request):
    phone=request.data.get("phone")
    try:
        user_obj=CustomUser.objects.get(phone=phone)
    except ObjectDoesNotExist as e:
        return response_400("There is no such Phone")
    password = request.data.get("password")
    if len(password) < 8:
        return response_400("Please send a valid Password (at least 8 digit)")
    user_obj.set_password(password)
    user_obj.save()
    return response_200(None)