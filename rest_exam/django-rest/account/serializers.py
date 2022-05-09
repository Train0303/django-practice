from dataclasses import fields
from rest_framework import serializers
from .models import User


# UserMakeSerializer로 바꾸기
class UserSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(use_url=True)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'username',
            'following',
            'profile',
        )
        extra_kwargs = {"password": {"write_only": True}}

# UserGetSerializer 만들어야함
class UserReadSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(use_url=True)
    class Meta:
        model = User
        fields = (
            'username',
            'profile',
        )