from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from django.db.models import Q

from users.models import CustomUser, Finrend


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_a_finrend(request):
    username_text = request.data.get('username')
    try:
        user_obj = CustomUser.objects.get(username=username_text)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    if request.user == user_obj:
        return response_400("You can't finrend yourself")
    try:
        Finrend.objects.get(Q(finrender_user=request.user, finrendered_user=user_obj, is_finrend_accepted=True) | Q(
            finrender_user=user_obj, finrendered_user=request.user, is_finrend_accepted=True) |Q(finrender_user=request.user, finrendered_user=user_obj, is_finrend_accepted=None) | Q(
            finrender_user=user_obj, finrendered_user=request.user, is_finrend_accepted=None))
        return response_400("This user already finrend you")
    except ObjectDoesNotExist as e:
        Finrend.objects.create(
            finrender_user=request.user,
            finrendered_user=user_obj
        )
        return response_200(None)
