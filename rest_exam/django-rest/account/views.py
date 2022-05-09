from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView
# @api_view(['GET','POST'])
# def user_list_create_api_view(request):
#     if (request.method) == "GET":
#         users = User.objects.filter(is_active = True)
#         serializer = UserSerializer(users,many=True)
#         return Response(serializer.data)
    
#     elif (request.method) == "POST":
#         serializer = UserSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def user_detail_api_view(request,username):
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return Response({"error":
#         {
#             "code" : 404,
#             "message" : "User not found"
#         }},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = UserSerializer(user,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         user.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)


class UserListAPIView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    

class UserDetailAPIView(APIView):
    def get_object(self,username):
        return get_object_or_404(User, username = username)

    def get(self,request,username,format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self,request,username):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,username):
        user = self.get_object(username)
        user.delete()
        return Response(stauts=status.HTTP_204_NO_CONTENT)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            qs = qs.filter(username__contains=search)
        
        return qs


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveAPIView):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
