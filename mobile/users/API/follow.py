# follow user
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from mobile.otp import check_otp
from mobile.responses import response_200, response_400, response_500
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token


from users.models import CustomUser, Followers


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request):
    username_text = request.data.get('username')
    try:
        user_obj = CustomUser.objects.get(username=username_text)
    except ObjectDoesNotExist as e:
        return response_400("There is no such user")
    if request.user == user_obj:
        return response_400("You can't follow yourself")
    try:
        follower_obj = Followers.objects.get(
            follower_user=request.user, followed_user=user_obj)
        return response_400("You already follow this user")
    except ObjectDoesNotExist as e:
        follower_obj = Followers.objects.create(
            follower_user=request.user,
            followed_user=user_obj
        )
        user_obj.followers_count += 1
        user_obj.save()
        request.user.following_count += 1
        request.user.save()
        return response_200(None)
