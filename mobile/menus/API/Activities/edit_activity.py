from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_activity(request):
    activity_id = request.data.get("activity_id")
    image = request.data.get("image")
    content = request.data.get("content")
    locked_comments = request.data.get("locked_comments")
    try:
        activity_obj = Activities.objects.get(id=activity_id)
    except ObjectDoesNotExist as e:
        return response_400("There is no such post")
    if activity_obj.user != request.user:
        return response_400("The post is not belongs to you")
    if type(image) != str:
        activity_obj.image = image
    activity_obj.content = content
    activity_obj.locked_comments = locked_comments
    activity_obj.save()
    return response_200(None)
