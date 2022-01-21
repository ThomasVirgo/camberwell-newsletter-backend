from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    gif = models.CharField(max_length=1000, blank=True)
    def __str__(self) -> str:
        return f'post: {self.title}'

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'comment:  {self.content}'

class Suggestion(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'post: {self.content}'

class SuggestionComment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'comment:  {self.content}'

class SuggestionVote(models.Model):
    up_vote = models.BooleanField(default=False)
    down_vote = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'lvote on {self.suggestion} on suggestion {self.suggestion}'

class PostLike(models.Model):
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


