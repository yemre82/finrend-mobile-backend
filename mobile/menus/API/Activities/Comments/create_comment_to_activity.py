from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities, ActivitiesComment
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment_to_activity(request):
    activity_id = request.data.get("activity_id")
    try:
        activity_obj = Activities.objects.get(id=activity_id)
    except ObjectDoesNotExist as e:
        return response_400("There is no such post")
    if activity_obj.locked_comments == True:
        return response_400("This post is locked comments")
    content = request.data.get("content")
    image = request.data.get("image")
    ActivitiesComment.objects.create(
        activity=activity_obj,
        user=request.user,
        image=image,
        content=content
    )
    activity_obj.comments_count += 1
    activity_obj.save()
    return response_200(None)
