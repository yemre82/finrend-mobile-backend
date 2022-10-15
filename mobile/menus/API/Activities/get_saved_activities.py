from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities, ActivitiesLike, BlockedActivities, SavedActivities
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_saved_activities(request):
    saved_activities_list = []
    saved_activities_obj = SavedActivities.objects.filter(user=request.user)
    for i in saved_activities_obj:
        is_mine = False
        if i.activity.user == request.user:
            is_mine = True
        try:
            like_obj = ActivitiesLike.objects.get(
                activity=i.activity,
                user=request.user
            )
            is_liked = False
        except ObjectDoesNotExist as e:
            is_liked = True
        try:
            SavedActivities.objects.get(activity=i.activity, user=request.user)
            is_saved = True
        except ObjectDoesNotExist as e:
            is_saved = False
        return_obj = {
            "activity_id": i.activity.id,
            "is_mine": is_mine,
            "is_liked": is_liked,
            "is_saved": is_saved,
            "username": i.activity.user.username,
            "followers": i.activity.user.followers_count,
            "image": "/media/"+str(i.activity.image),
            "content": i.activity.content,
            "likes_count": i.activity.likes_count,
            "comments_count": i.activity.comments_count,
            "locked_comments": i.activity.locked_comments,
            "created_at": i.activity.created_at,
            "updated_at": i.activity.updated_at
        }
        saved_activities_list.append(return_obj)
    return response_200(saved_activities_list)
