from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities, ActivitiesComment
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_activities_comments(request):
    comments_list = []
    activity_id = request.data.get("activity_id")
    try:
        activity_obj = Activities.objects.get(id=activity_id)
    except ObjectDoesNotExist as e:
        return response_400("There is no such post")
    if activity_obj.locked_comments == True:
        return response_400("There is no comment for this post")
    comments_obj = ActivitiesComment.objects.filter(activity=activity_obj)
    for i in comments_obj:
        is_mine = False
        if i.user == request.user:
            is_mine = True
        return_obj = {
            "comments_id": i.id,
            "is_mine": is_mine,
            "user": i.user.username,
            "image": "/media/"+str(i.image),
            "content": i.content,
            "created_at": i.created_at,
            "updated_at": i.updated_at
        }
        comments_list.append(return_obj)
    return response_200(comments_list)
