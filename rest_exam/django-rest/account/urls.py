from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'^user',UserViewSet)

urlpatterns = [
    path(r'^',include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)