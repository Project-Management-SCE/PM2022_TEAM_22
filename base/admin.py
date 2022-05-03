from django.contrib import admin

# from base.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Favorite

# admin.site.register(Room)
# admin.site.register(Topic)
# admin.site.register(Message)
admin.site.register(Favorite)
# admin.site.register(Account)
# class AccountInline(admin.StackedInline):
#  can_delete = False
# verbose_name_plural = 'Accounts'

# class CustomizedUserAdmin(UserAdmin):
#   inlines = (AccountInline,)

# admin.site.unregister(User)
# admin.site.register(User,CustomizedUserAdmin)
