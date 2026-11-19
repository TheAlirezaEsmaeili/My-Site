from django.contrib.auth.views import LogoutView
from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("blog/<int:pk>/like/", views.like_post, name="like_post"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.VlogLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
]
