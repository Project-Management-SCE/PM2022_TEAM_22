from django.contrib import admin

# from base.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Favorite


admin.site.register(Favorite)
