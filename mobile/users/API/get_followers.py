from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from users.models import CustomUser, Followers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_followers(request,username_text):
    try:
        user_obj=CustomUser.objects.get(username=username_text)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    followers=Followers.objects.filter(followed_user=user_obj)
    returning_list=[]
    for i in followers:
        is_me=False
        if i.follower_user==request.user:
            is_me=True
        return_obj={
            "is_me":is_me,
            "phone":i.follower_user.phone,
            "email":i.follower_user.email,
            "gender":i.follower_user.gender,
            "firstname":i.follower_user.firstname,
            "lastname":i.follower_user.lastname,
            "username":i.follower_user.username,
            "birthday":i.follower_user.birthday,
            "followers_count":i.follower_user.followers_count,
            "following_count":i.follower_user.following_count,
            "location":i.follower_user.location,
            "website":i.follower_user.website,
            "biograpyh":i.follower_user.biograpyh,
            "qr_code":i.follower_user.qr_code,
            "created_at":i.follower_user.created_at,
            "updated_at":i.follower_user.updated_at
        }
        returning_list.append(return_obj)
    return response_200(returning_list)