from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities, ActivitiesComment
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_comment(request):
    comment_id = request.data.get("comment_id")
    try:
        comment_obj = ActivitiesComment.objects.get(id=comment_id)
    except ObjectDoesNotExist as e:
        return response_400("there is no such comment")
    if comment_obj.user != request.user:
        return response_400("This comment is not belongs to you")
    comment_obj.delete()
    return response_200(None)
