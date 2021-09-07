from django.contrib import admin
from django.contrib.admin.sites import site
from django.contrib.auth.models import User
from .models import Userprofile
# Register your models here.

site.register(Userprofile)
