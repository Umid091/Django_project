from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.admin.blog.serializer import *
from blog.models import Post


class BlogListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]