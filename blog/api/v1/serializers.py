from rest_framework import serializers
from django.utils import timezone

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    published_at = serializers.DateTimeField(label="تاریخ انتشار", default=timezone.now)
    content = serializers.CharField(label="متن کامل",max_length=500)
