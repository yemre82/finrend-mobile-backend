from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from users.models import CustomUser, OTPRegister
from users.utils import generate_random_num, send_email


@api_view(['POST'])
@permission_classes([AllowAny])
def register_email(request):
    otp = request.headers["OTP"]
    if check_otp(str(otp)) == "OTP is not True":
        return response_400("Please send a valid OTP")
    email = request.data.get("email")
    try:
        CustomUser.objects.get(email=email)
    except ObjectDoesNotExist as e:
        return response_400("Email is already exist")
    username = request.data.get("username")
    try:
        CustomUser.objects.get(username=username)
    except ObjectDoesNotExist as e:
        return response_400("Username is already exist")
    birthday = datetime.strptime(request.data.get("birthday"), "%Y-%m-%d")
    firstname = request.data.get("firstname")
    if len(firstname) == 0:
        return response_400("Please send a valid firstname")
    lastname = request.data.get("lastname")
    if len(lastname) == 0:
        return response_400("Please send a valid lastname")
    gender = request.data.get("gender")
    if len(gender) == 0:
        return response_400("Please send a valid gender")
    password = request.data.get("password")
    if len(password) < 8:
        return response_400("Please send a valid Password (at least 8 digit)")
    user_obj = CustomUser.objects.create(
        email=email,
        username=username,
        birthday=birthday,
        firstname=firstname,
        lastname=lastname,
        gender=gender
    )
    user_obj.set_password(password)
    user_obj.save()
    otp = generate_random_num()
    description_obj = "email verification"
    OTPRegister.objects.create(
        user=user_obj,
        otp=str(otp),
        description=description_obj
    )
    send_email(user_obj.email, otp,
               "Email Verification of Finrend")
    return response_200(None)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_phone(request):
    otp = request.headers["OTP"]
    if check_otp(str(otp)) == "OTP is not True":
        return response_400("Please send a valid OTP")
    phone = request.data.get("phone")
    try:
        CustomUser.objects.get(phone=phone)
    except ObjectDoesNotExist as e:
        return response_400("Phone is already exist")
    username = request.data.get("username")
    try:
        CustomUser.objects.get(username=username)
    except ObjectDoesNotExist as e:
        return response_400("Username is already exist")
    birthday = datetime.strptime(request.data.get("birthday"), "%Y-%m-%d")
    firstname = request.data.get("firstname")
    if len(firstname) == 0:
        return response_400("Please send a valid firstname")
    lastname = request.data.get("lastname")
    if len(lastname) == 0:
        return response_400("Please send a valid lastname")
    gender = request.data.get("gender")
    if len(gender) == 0:
        return response_400("Please send a valid gender")
    password = request.data.get("password")
    if len(password) < 8:
        return response_400("Please send a valid Password (at least 8 digit)")
    user_obj = CustomUser.objects.create(
        phone=phone,
        username=username,
        birthday=birthday,
        firstname=firstname,
        lastname=lastname,
        gender=gender
    )
    user_obj.set_password(password)
    otp = generate_random_num()
    description_obj = "phone verification"
    OTPRegister.objects.create(
        user=user_obj,
        otp=str(otp),
        description=description_obj
    )
    # sms gönder
    return response_200(None)
