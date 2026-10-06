from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404
from rest_framework import status
from blog.models import Post

class PostList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self,request,):
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request,id):
        post = get_list_or_404(post,pk=id,status=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self,request,id):
        post = get_list_or_404(post,pk=id,status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        post = get_list_or_404(post,pk=id,status=True)
        post.delete()
        return Response('deleted',status=status.HTTP_204_NO_CONTENT)


        