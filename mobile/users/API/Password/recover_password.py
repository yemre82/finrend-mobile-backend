from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from users.models import CustomUser, OTPForgotPassword


@api_view(['POST'])
@permission_classes([AllowAny])
def recover_password_email(request):
    email = request.data.get("email")
    try:
        user_obj = CustomUser.objects.get(email=email)
    except ObjectDoesNotExist as e:
        return response_400("There is no such Email")
    otp = request.data.get("otp")
    try:
        otp_forgot_obj = OTPForgotPassword.objects.get(user=user_obj, otp=otp)
    except ObjectDoesNotExist as e:
        return response_400("There is no such OTP")
    otp_forgot_obj.is_verified = True
    otp_forgot_obj.save()
    return response_200(None)


@api_view(['POST'])
@permission_classes([AllowAny])
def recover_password_phone(request):
    phone = request.data.get("phone")
    try:
        user_obj = CustomUser.objects.get(phone=phone)
    except ObjectDoesNotExist as e:
        return response_400("There is no such Phone")
    otp = request.data.get("otp")
    try:
        otp_forgot_obj = OTPForgotPassword.objects.get(user=user_obj, otp=otp)
    except ObjectDoesNotExist as e:
        return response_400("There is no such OTP")
    otp_forgot_obj.is_verified = True
    otp_forgot_obj.save()
    return response_200(None)
