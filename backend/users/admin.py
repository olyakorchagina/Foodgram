from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Subscription, User


class UserAdmin(UserAdmin):
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
        'password',
    )
    list_filter = (
        'email',
        'username',
    )
    search_fields = (
        'email',
        'username',
    )
    empty_value_display = '-пусто-'


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'subscriber',
        'target',
    )
    list_filter = (
        'subscriber',
        'target',
    )
    search_fields = (
        'subscriber',
        'target',
    )
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
