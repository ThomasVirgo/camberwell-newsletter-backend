from rest_framework import viewsets
from .models import Post, CommentLike, Comment, PostLike
from .serializers import PostSerializer, PostLikeSerializer, CommentLikeSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comment instances.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentLikeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post like instances.
    """
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

class PostLikeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comment like instances.
    """
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()