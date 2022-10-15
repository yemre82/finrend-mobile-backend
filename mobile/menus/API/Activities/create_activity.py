from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from menus.models import Activities
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_activity(request):
    image = request.data.get("image")
    content = request.data.get("content")
    locked_comments = request.data.get("locked_comments")
    Activities.objects.create(
        user=request.user,
        image=image,
        content=content,
        locked_comments=locked_comments
    )

    return response_200(None)
