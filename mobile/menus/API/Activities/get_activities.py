from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities, ActivitiesLike, BlockedActivities, SavedActivities
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist

from users.models import Followers



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_activities(request):
    activities_list=[]
    followers_obj=Followers.objects.filter(follower_user=request.user)
    for i in followers_obj:
        activities_obj=Activities.objects.filter(user=i.followed_user)
        for j in activities_obj:
            try:
                BlockedActivities.objects.get(activity=j,user=request.user)
            except ObjectDoesNotExist as e:
                is_mine=False
                if j.user==request.user:
                    is_mine=True
                is_liked=False
                try:
                    ActivitiesLike.objects.get(activity=j,user=request.user)
                    is_liked=True
                except ObjectDoesNotExist as e:
                    is_liked=False
                try:
                    SavedActivities.objects.get(activity=j,user=request.user)
                    is_saved=True
                except ObjectDoesNotExist as e:
                    is_saved=False
                return_obj={
                    "activity_id":j.id,
                    "is_mine":is_mine,
                    "is_liked":is_liked,
                    "is_saved":is_saved,
                    "username":j.user.username,
                    "followers":j.user.followers_count,
                    "image":"/media/"+str(j.image),
                    "content":j.content,
                    "likes_count":j.likes_count,
                    "comments_count":j.comments_count,
                    "locked_comments":j.locked_comments,
                    "created_at":j.created_at,
                    "updated_at":j.updated_at
                }
                activities_list.append(return_obj)
    return response_200(activities_list)