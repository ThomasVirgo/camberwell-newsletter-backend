from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='posts', storage=gd_storage)
    def __str__(self) -> str:
        return f'post: {self.title}'


class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'comment:  {self.content}'


class PostLike(models.Model):
    # change this to use choices, see drf documentation
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    laugh = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'like from {self.from_user} on post {self.post}'


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    laugh = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'like from {self.from_user} on comment {self.comment}'

class Meal(models.Model):
    title = models.CharField(max_length = 200)
    made_by = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='posts', storage=gd_storage)
    def __str__(self) -> str:
        return f'post: {self.title}'

class MealComment(models.Model): # need to add validation that they havent already made a comment
    content = models.TextField()
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
     )
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="comments")
    def __str__(self) -> str:
        return f'comment:  {self.content}'


