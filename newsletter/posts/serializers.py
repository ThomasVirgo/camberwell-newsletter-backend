from rest_framework import serializers
from .models import Post, Comment, PostLike, CommentLike

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
