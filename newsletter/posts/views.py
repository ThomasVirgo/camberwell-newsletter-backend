from rest_framework import viewsets
from .models import Post, CommentLike, Comment, PostLike, Meal, MealComment
from .serializers import PostSerializer, PostLikeSerializer, CommentLikeSerializer, CommentSerializer, MealCommentSerializer, MealSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model

class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=False, methods=['post'])
    def add_post_by_email(self, request):
        user_model = get_user_model()
        user = user_model.objects.get(email=request.data['author']) # use get when getting single object, use filter when getting multiple
        new_data = request.data
        new_data['author'] = user.id
        serializer = PostSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    @action(detail=True)
    def comments_on_post(self, request, pk):
        comments = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def add_comment_by_email(self, request):
        user_model = get_user_model()
        user = user_model.objects.get(email=request.data['author'])
        new_data = request.data
        new_data['author'] = user.id
        serializer = CommentSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentLikeViewSet(viewsets.ModelViewSet):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

class PostLikeViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()

class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

class MealCommentViewSet(viewsets.ModelViewSet):
    serializer_class = MealCommentSerializer
    queryset = MealComment.objects.all()

    @action(detail=True)
    def comments_on_post(self, request, pk):
        comments = MealComment.objects.filter(meal=pk)
        serializer = MealCommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add_comment_by_email(self, request):
        user_model = get_user_model()
        user = user_model.objects.get(email=request.data['author'])
        new_data = request.data
        new_data['author'] = user.id
        serializer = MealCommentSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
