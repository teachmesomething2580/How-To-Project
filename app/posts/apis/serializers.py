from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin

from posts.models import PostCategory, Post, PostComment


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'


class PostSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = (
            'deleted_at',
            'like_users',
        )
        read_only_fields = (
            'author',
            'like_users',
        )

    def create(self, validated_data):
        author = self.context.get('request').user

        instance = Post.objects.create(
            author=author,
            **validated_data
        )

        return instance


class PostCommentSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'id',
            'post',
            'author',
            'parent',
            'content',
        )
        read_only_fields = (
            'post',
            'author',
            'parent',
        )

    def create(self, validated_data):
        author = self.context.get('request').user
        post = get_object_or_404(Post.objects.filter(deleted_at=None),
                                 pk=self.context.get('view').kwargs.get('pk'))

        instance = PostComment.objects.create(
            author=author,
            post=post,
            **validated_data,
        )

        return instance
