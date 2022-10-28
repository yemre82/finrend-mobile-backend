from django.urls import path
from users.API.Password.new_password import new_password_email, new_password_phone
from users.API.accept_a_finrend import accept_a_finrend
from users.API.get_all_notification_finrend import get_all_notification_finrend

from users.API.register import register_email, register_phone
from users.API.login import login
from users.API.get_profile import get_profile
from users.API.get_followers import get_followers
from users.API.get_followings import get_followings
from users.API.follow import follow
from users.API.reject_a_finrend import reject_a_finrend
from users.API.send_a_finrend import send_a_finrend
from users.API.unfollow import unfollow
from users.API.verify_user import verify_email, verify_phone
from users.API.CheckUser.check_email import check_email
from users.API.CheckUser.check_phone import check_phone
from users.API.CheckUser.check_username import check_username
from users.API.Password.forgot_password import forgot_password_email, forgot_password_phone
from users.API.Password.recover_password import recover_password_email, recover_password_phone

urlpatterns = [
    path("register-email",register_email),
    path("register-phone",register_phone),
    path("login",login),
    path("get-profile/<str:username_text>",get_profile),
    path("get-followers/<str:username_text>",get_followers),
    path("get-followings/<str:username_text>",get_followings),
    path("follow",follow),
    path("unfollow",unfollow),
    path("verify-email",verify_email),
    path("verify-phone/<str:phone_text/<str:otp_text",verify_phone),
    path("check-email",check_email),
    path("check-phone",check_phone),
    path("check-username",check_username),
    path("forgot-password-email",forgot_password_email),
    path("forgot-password-phone",forgot_password_phone),
    path("recover-password-email",recover_password_email),
    path("recover-password-phone",recover_password_phone),
    path("new-password-email",new_password_email),
    path("new-password-phone",new_password_phone),
    path("send-a-finrend",send_a_finrend),
    path("reject-a-finrend",reject_a_finrend),
    path("get-all-notification-finrend",get_all_notification_finrend),
    path("accept-a-finrend",accept_a_finrend),
]