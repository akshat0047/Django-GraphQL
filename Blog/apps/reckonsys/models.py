from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.TextField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.TextField()
