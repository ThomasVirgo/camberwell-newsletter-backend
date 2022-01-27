from rest_framework import viewsets
from .models import Post, CommentLike, Comment, PostLike, Suggestion, SuggestionComment, SuggestionVote
from .serializers import PostSerializer, PostLikeSerializer, CommentLikeSerializer, CommentSerializer, SuggestionSerializer, SuggestionCommentSerializer, SuggestionVoteSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentLikeViewSet(viewsets.ModelViewSet):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

class PostLikeViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()

class SuggestionViewSet(viewsets.ModelViewSet):
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.all()

class SuggestionCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    queryset = SuggestionComment.objects.all()

class SuggestionVoteViewSet(viewsets.ModelViewSet):
    serializer_class = SuggestionVoteSerializer
    queryset = SuggestionVote.objects.all()