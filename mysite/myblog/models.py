from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class myblog(models.Model):
    class Meta():
        db_table = "myblog"
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

class comments(models.Model):
    class Meta():
        db_table = 'comment'
    comments_text = models.TextField()
    comments_myblog = models.ForeignKey(myblog, on_delete=models.CASCADE)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
