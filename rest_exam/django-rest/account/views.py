from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            qs = qs.filter(username__contains=search)
        
        return qs

