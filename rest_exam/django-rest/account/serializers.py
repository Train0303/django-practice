from rest_framework import serializers
from .models import User

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