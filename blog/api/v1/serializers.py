from rest_framework import serializers
from django.utils import timezone
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','author','status','content','published_at']