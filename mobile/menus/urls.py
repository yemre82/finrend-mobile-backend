from django.urls import path
from menus.API.Activities.Comments.create_comment_to_activity import create_comment_to_activity
from menus.API.Activities.Comments.delete_comment import delete_comment
from menus.API.Activities.Comments.edit_comment import edit_comment
from menus.API.Activities.Comments.get_activity_comments import get_activities_comments

from menus.API.Activities.block_activity import block_activity
from menus.API.Activities.create_activity import create_activity
from menus.API.Activities.delete_activity import delete_activity
from menus.API.Activities.edit_activity import edit_activity
from menus.API.Activities.get_activities import get_activities
from menus.API.Activities.get_activity import get_activity
from menus.API.Activities.get_saved_activities import get_saved_activities
from menus.API.Activities.get_user_activity import get_user_activity
from menus.API.Activities.like_activity import like_activity
from menus.API.Activities.save_activity import save_activity
from menus.API.Activities.unblock_activity import unblock_activity
from menus.API.Activities.unsave_activity import unsave_activity


urlpatterns = [
    path("block-activity/<int:activity_id>",block_activity),
    path("create-activity",create_activity),
    path("delete-activity",delete_activity),
    path("edit-activity",edit_activity),
    path("get-activities",get_activities),
    path("get-activity",get_activity),
    path("get-saved-activities",get_saved_activities),
    path("get-user-activity/<str:username_text>",get_user_activity),
    path("like-activity/<int:activity_id>",like_activity),
    path("save-activity/<int:activity_id>",save_activity),
    path("unsave-activity/<int:activity_id>",unsave_activity),
    path("unblock-activity/<int:activity_id>",unblock_activity),
    path("create-comment-to-activity",create_comment_to_activity),
    path("delete-comment",delete_comment),
    path("edit-comment",edit_comment),
    path("get-activities-comments",get_activities_comments),
]