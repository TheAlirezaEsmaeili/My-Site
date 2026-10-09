from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet

router = DefaultRouter()
app_name = "api_v1"

router.register('post',views.PostModelViewSet,basename='post')
urlpatterns = router.urls
