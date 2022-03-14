from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserChangeForm
from .models import User
# Register your models here.

admin.site.register(User)
admin.site.unregister(Group)