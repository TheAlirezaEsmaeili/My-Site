from rest_framework import serializers
from django.utils import timezone
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','author','status','content','published_at']

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('status',None)
        else:
            rep.pop('content',None)
        return rep