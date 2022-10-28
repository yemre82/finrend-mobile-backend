from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from django.db.models import Q

from users.models import CustomUser, Followers, Portfolio, Finrend


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request,username_text):
    try:
        user_obj=CustomUser.objects.get(username=username_text,is_active=True)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    is_me=False
    if user_obj==request.user:
        is_me=True
    can_finrend=False
    portfolio_list=[]
    if is_me:
        portfolio_obj=Portfolio.objects.filter(user=user_obj)
        for i in portfolio_obj:
            return_obj={
                "portfolio_id":i.id,
                "user":i.user.username,
                "portfolio_coin_id":i.portfolio_description,
                "created_at":i.created_at,
                "updated_at":i.updated_at,
            }
            portfolio_list.append(return_obj)
    else:
        try:
            finrend_obj=Finrend.objects.get(Q(finrender_user=request.user,finrendered_user=user_obj,is_finrend_accepted=True)|Q(finrender_user=user_obj,finrendered_user=request.user,is_finrend_accepted=True))
            if finrend_obj.finrender_user==user_obj:
                portfolio_obj=Portfolio.objects.filter(user=user_obj)
                for i in portfolio_obj:
                    return_obj={
                        "portfolio_id":i.id,
                        "user":i.user.username,
                        "portfolio_coin_id":i.portfolio_description,
                        "created_at":i.created_at,
                        "updated_at":i.updated_at,
                    }
                    portfolio_list.append(return_obj)
            elif finrend_obj.finrendered_user==user_obj:
                portfolio_obj=Portfolio.objects.filter(user=user_obj)
                for i in portfolio_obj:
                    return_obj={
                        "portfolio_id":i.id,
                        "user":i.user.username,
                        "portfolio_coin_id":i.portfolio_description,
                        "created_at":i.created_at,
                        "updated_at":i.updated_at,
                    }
                    portfolio_list.append(return_obj)
        except ObjectDoesNotExist as e:
            portfolio_list=[]
            can_finrend=True
    try:
        Followers.objects.get(follower_user=request.user,followed_user=user_obj)
        is_following=True
    except ObjectDoesNotExist as e:
        is_following=False
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
        "portfolio":portfolio_list,
        "can_finrend":can_finrend,
        "is_following":is_following,
        "created_at":user_obj.created_at,
        "updated_at":user_obj.updated_at
    }
    return response_200(return_obj)
