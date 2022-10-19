from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from users.models import CustomUser, Finrend

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_notification_finrend(request):
    finrend_obj = Finrend.objects.filter(finrendered_user=request.user,is_finrend_accepted=None)
    finrend_list = []
    for finrend in finrend_obj:
        return_obj={
            "finrender_user":finrend.finrender_user.username,
            "finrendered_user":finrend.finrendered_user.username,
            "finrend_id":finrend.id,
            "finrend_created_at":finrend.created_at,
            "is_finrend_accepted":finrend.is_finrend_accepted,
        }
        finrend_list.append(return_obj)
    return response_200(finrend_list)
    