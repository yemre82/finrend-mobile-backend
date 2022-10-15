from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities, SavedActivities
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def save_activity(request, activity_id):
    try:
        activity_obj = Activities.objects.get(id=activity_id)
    except ObjectDoesNotExist as e:
        return response_400("There is no such post")
    try:
        saved_obj = SavedActivities.objects.get(
            activity=activity_obj,
            user=request.user
        )
        return response_400("The post is already saved")
    except ObjectDoesNotExist as e:
        if activity_obj.user == request.user:
            return response_400("You can't save this post because it belongs to you")
        SavedActivities.objects.create(
            activity=activity_obj,
            user=request.user
        )
    return response_200(None)
