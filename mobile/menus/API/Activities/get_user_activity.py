#getting user activities
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from users.models import CustomUser
from menus.models import Activities

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_activity(request,username_text):
    try:
        user_obj=CustomUser.objects.get(username=username_text)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    activity_objs=Activities.objects.filter(user=user_obj)
    return_obj=[]
    for activity_obj in activity_objs:
        return_obj.append({
            "id":activity_obj.id,
            "user":activity_obj.user.username,
            "image":"/media/"+str(activity_obj.image),
            "content":activity_obj.content,
            "likes_count":activity_obj.likes_count,
            "comments_count":activity_obj.comments_count,
            "locked_comments":activity_obj.locked_comments,
            "created_at":activity_obj.created_at,
            "updated_at":activity_obj.updated_at
        })
    return response_200(return_obj)