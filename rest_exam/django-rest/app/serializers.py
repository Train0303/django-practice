from rest_framework import serializers
from .models import Post,PostImage
from account.serializers import UserSerializer
from account.models import User
class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']

class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    writer = UserSerializer(read_only = True)
    
    def get_images(self,obj):
        image_data = obj.images
        return PostImageSerializer(instance=image_data, many = True,context=self.context,read_only=True).data

    class Meta:
        model = Post
        fields = ['writer','id','title','content','create_at','images']
    
    
    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            PostImage.objects.create(post=instance,image=image_data)
        return instance