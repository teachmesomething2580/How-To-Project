from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.apis.serializers import PostCategorySerializer, PostSerializer
from posts.models import PostCategory, Post


class PostCategoryListGenericAPIView(generics.ListAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class PostListCreateGenericAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostLikeToggleAPIView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post.objects.all(), pk=kwargs.get('pk'))
        status = post.like_toggle(request.user)
        return Response(status=status)