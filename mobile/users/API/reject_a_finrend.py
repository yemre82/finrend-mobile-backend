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
def reject_a_finrend(request):
    finrend_id = request.data.get('finrend_id')
    try:
        finrend_obj = Finrend.objects.get(id=finrend_id)
    except ObjectDoesNotExist as e:
        return response_400("There is no such finrend")
    if request.user != finrend_obj.finrendered_user:
        return response_400("You can't reject this finrend")
    if finrend_obj.is_finrend_accepted!=None:
        return response_400("This finrend is already accepted or rejected")
    finrend_obj.is_finrend_accepted = False
    finrend_obj.save()
    return response_200(None)