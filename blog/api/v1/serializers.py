from rest_framework import serializers
from django.utils import timezone
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):

    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')

    class Meta:
        model = Post
        fields = ['title','author','status','content','absolute_url','published_at']

    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('status',None)
            rep.pop('absolute_url',None)
        else:
            rep.pop('content',None)
        return rep