from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'post_comments', views.CommentViewSet, basename='comment')
router.register(r'post_likes', views.PostLikeViewSet, basename='post like')
router.register(r'comment_likes', views.CommentLikeViewSet, basename='comment like')

router.register(r'meals', views.MealViewSet, basename='meal')
router.register(r'meal_comments', views.MealCommentViewSet, basename='meal comment')

urlpatterns = router.urls