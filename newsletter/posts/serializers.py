from rest_framework import serializers
from .models import Post, Comment, PostLike, CommentLike, Meal, MealComment
from .send_mail import create_and_send_mail

class PostSerializer(serializers.ModelSerializer):
    author_names = serializers.SerializerMethodField()
    type = serializers.ReadOnlyField(default='post')

    class Meta:
        model = Post
        fields = "__all__"
    
    def get_author_names(self, obj):
        return {
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name
        }
    
class CommentSerializer(serializers.ModelSerializer):
    author_names = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_author_names(self, obj):
        return {
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name
        }

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = "__all__"


class MealCommentSerializer(serializers.ModelSerializer):
    author_names = serializers.SerializerMethodField()
    class Meta:
        model = MealComment
        fields = "__all__"
    def get_author_names(self, obj):
        return {
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name
        }
    def validate(self, data):
        """
        Check that the user has not already created a comment on that meal.
        """
        user_comments = MealComment.objects.filter(author=data['author'].id, meal=data['meal'].id)
        if len(user_comments) > 0:
            raise serializers.ValidationError("User has already created a comment on this meal.")
        return data

class MealSerializer(serializers.ModelSerializer):
    type = serializers.ReadOnlyField(default='meal')
    # must make sure that you have the related name set in the model and this must match the variable name
    comments = serializers.SlugRelatedField(
            many=True, 
            read_only=True,
            slug_field="rating"
    )
    # comments = MealCommentSerializer(many=True)
    class Meta:
        model = Meal
        fields = "__all__"
        