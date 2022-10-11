from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist

from users.models import CustomUser

@api_view(['POST'])
@permission_classes([AllowAny])
def check_username(request):
    username=request.data.get("username")
    try:
        CustomUser.objects.get(username=username)
    except ObjectDoesNotExist as e:
        return response_400("Username is already exist")
    return response_200(None)
