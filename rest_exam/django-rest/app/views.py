from django.shortcuts import render
from rest_framework import viewsets,serializers
from .serializers import PostImageSerializer, PostSerializer
from rest_framework.views import APIView
from .models import Post,PostImage
from account.models import User
# Create your views here.



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        user = User.objects.get(username = self.request.data['writer'])
        serializer.save(writer = user)

class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    
