from django.urls import path,include
from . import views

app_name = "api_v1"

urlpatterns = [
    path('post/',views.PostList.as_view(),name='post_list'),
    path('post/<int:id>/',views.PostDetail.as_view(),name='post_detail'),
]