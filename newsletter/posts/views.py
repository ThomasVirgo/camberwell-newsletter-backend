from rest_framework import viewsets
from .models import Post, CommentLike, Comment, PostLike
from .serializers import PostSerializer, PostLikeSerializer, CommentLikeSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()