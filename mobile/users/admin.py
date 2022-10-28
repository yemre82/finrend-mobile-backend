from django.contrib import admin

from users.models import CustomUser, Finrend
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class FinrendAdmin(admin.ModelAdmin):
    list_display = ('id', 'finrender_user', 'finrendered_user', 'is_finrend_accepted', 'created_at', 'updated_at')
    search_fields = ('id', 'finrender_user',"finrendered_user")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Finrend, FinrendAdmin)


class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'created_at',
                    'updated_at', 'is_admin', 'is_staff',"is_active")
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, UserAdmin)