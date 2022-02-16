from rest_framework import serializers
from .models import Post, Comment, PostLike, CommentLike, Suggestion, SuggestionComment, SuggestionVote

class PostSerializer(serializers.ModelSerializer):
    author_names = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
    
    def get_author_names(self, obj):
        return {
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name
        }
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = "__all__"

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = "__all__"

class SuggestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionComment
        fields = "__all__"

class SuggestionVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionVote
        fields = "__all__"