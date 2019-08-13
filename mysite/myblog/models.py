from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class myblog(models.Model):
    class Meta():
        db_table = "myblog"
    myblog_title = models.CharField(max_length = 200)
    myblog_text = models.TextField()
    myblog_date = models.DateTimeField()
    myblog_likes = models.IntegerField()


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
