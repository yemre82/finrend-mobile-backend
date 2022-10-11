from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from users.models import CustomUser, OTPRegister


@api_view(['GET'])
@permission_classes([AllowAny])
def verify_email(request, email_text, otp_text):
    try:
        user_obj = CustomUser.objects.get(email=email_text)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    otp_obj = OTPRegister.objects.filter(user=user_obj, otp=otp_text)
    if len(otp_obj) == 0:
        return response_400("There is no such otp")
    for i in otp_obj:
        try:
            user_obj = CustomUser.objects.get(id=i.user.id)
        except ObjectDoesNotExist as e:
            return response_400("There is no such user")
        user_obj.is_active = True
        user_obj.save()
        i.is_verified = True
        i.save()
    return response_200(None)


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_phone(request, phone_text, otp_text):
    try:
        user_obj = CustomUser.objects.get(phone=phone_text)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    otp_obj = OTPRegister.objects.filter(user=user_obj, otp=otp_text)
    if len(otp_obj) == 0:
        return response_400("There is no such otp")
    for i in otp_obj:
        try:
            user_obj = CustomUser.objects.get(id=i.user.id)
        except ObjectDoesNotExist as e:
            return response_400("There is no such user")
        user_obj.is_active = True
        user_obj.save()
        i.is_verified = True
        i.save()
    return response_200(None)
