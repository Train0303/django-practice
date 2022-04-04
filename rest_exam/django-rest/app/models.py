from django.db import models
from account.models import User
# Create your models here.

class Post(models.Model):
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updata_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"f{self.content}" 

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name = "images")
    image = models.ImageField(upload_to = 'postimage/',blank = True)