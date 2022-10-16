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
def get_followings(request, username_text):

    try:
        user_obj = CustomUser.objects.get(username=username_text)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    followings = Followers.objects.filter(follower_user=user_obj)
    returning_list = []
    for i in followings:
        is_me = False
        if i.followed_user == request.user:
            is_me = True
        return_obj = {
            "is_me": is_me,
            "phone": i.followed_user.phone,
            "email": i.followed_user.email,
            "gender": i.followed_user.gender,
            "firstname": i.followed_user.firstname,
            "lastname": i.followed_user.lastname,
            "username": i.followed_user.username,
            "birthday": i.followed_user.birthday,
            "followers_count": i.followed_user.followers_count,
            "following_count": i.followed_user.following_count,
            "location": i.followed_user.location,
            "website": i.followed_user.website,
            "biograpyh": i.followed_user.biograpyh,
            "qr_code": i.followed_user.qr_code,
            "created_at": i.followed_user.created_at,
            "updated_at": i.followed_user.updated_at
        }
        returning_list.append(return_obj)
    return response_200(returning_list)
