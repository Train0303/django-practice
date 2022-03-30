from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework import routers
# from .views import UserViewSet
# from .views import user_list_create_api_view,user_detail_api_view
from .views import UserListAPIView,UserDetailAPIView

router = routers.DefaultRouter()
# router.register(r'^user',UserViewSet)
# router.register(r'^user/',user_list_create_api_view,basename="userlist")
# router.register(r'^user/<str:username>/',user_detail_api_view,basename="userdetail")

urlpatterns = [
    path(r'^',include(router.urls)),
    path(r"user",UserListAPIView.as_view()),
    path(r"user/<str:username>",UserDetailAPIView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)