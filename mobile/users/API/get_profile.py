from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from users.models import CustomUser


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request,username_text):
    try:
        user_obj=CustomUser.objects.get(username=username_text)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    is_me=False
    if user_obj==request.user:
        is_me=True
    return_obj={
        "is_me":is_me,
        "phone":user_obj.phone,
        "email":user_obj.email,
        "gender":user_obj.gender,
        "firstname":user_obj.firstname,
        "lastname":user_obj.lastname,
        "username":user_obj.username,
        "birthday":user_obj.birthday,
        "followers_count":user_obj.followers_count,
        "following_count":user_obj.following_count,
        "location":user_obj.location,
        "website":user_obj.website,
        "biograpyh":user_obj.biograpyh,
        "qr_code":user_obj.qr_code,
        "created_at":user_obj.created_at,
        "updated_at":user_obj.updated_at
    }
    return response_200(return_obj)
