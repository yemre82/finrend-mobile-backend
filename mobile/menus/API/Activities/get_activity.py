from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities, ActivitiesLike, SavedActivities
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_activity(request):
    activity_id = request.data.get("activity_id")
    try:
        activity_obj = Activities.objects.get(id=activity_id)
    except ObjectDoesNotExist as e:
        return response_400("There is no such post")
    is_mine = False
    if activity_obj.user == request.user:
        is_mine = True
    try:
        like_obj = ActivitiesLike.objects.get(
            activity=activity_obj,
            user=request.user
        )
        is_liked = False
    except ObjectDoesNotExist as e:
        is_liked = True
    try:
        SavedActivities.objects.get(activity=activity_obj, user=request.user)
        is_saved = True
    except ObjectDoesNotExist as e:
        is_saved=False
    return_obj = {
        "activity_id": activity_obj.id,
        "is_mine": is_mine,
        "is_liked": is_liked,
        "is_saved":is_saved,
        "username": activity_obj.user.username,
        "followers": activity_obj.user.followers_count,
        "image": "/media/"+str(activity_obj.image),
        "content": activity_obj.content,
        "likes_count": activity_obj.likes_count,
        "comments_count": activity_obj.comments_count,
        "locked_comments": activity_obj.locked_comments,
        "created_at": activity_obj.created_at,
        "updated_at": activity_obj.updated_at
    }
    return response_200(return_obj)
