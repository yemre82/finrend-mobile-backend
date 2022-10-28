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
def login(request):
    otp = request.headers["OTP"]
    if check_otp(str(otp)) == "OTP is not True":
        return response_400("Please send a valid OTP")
    username = request.data.get("username")
    password = request.data.get("password")
    try:
        user_obj = CustomUser.objects.get(username=username)
    except ObjectDoesNotExist as e:
        try:
            user_obj = CustomUser.objects.get(email=username)
        except ObjectDoesNotExist as e:
            try:
                user_obj = CustomUser.objects.get(phone=username)
            except ObjectDoesNotExist as e:
                return response_400("There is no such User")
    if not user_obj.is_active:
        return response_400("Please verify your account")
    if not user_obj.check_password(password):
        return response_400("Password is not True")
    token, _ = Token.objects.get_or_create(user=user_obj)
    return_obj = {
        "token": token.key
    }
    return response_200(return_obj)
