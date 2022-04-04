from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework import routers
from .views import PostViewSet,PostImageViewSet

router = routers.DefaultRouter()
router.register('post',PostViewSet)
router.register('postimage',PostImageViewSet)
urlpatterns = [
    path('',include(router.urls)),
]