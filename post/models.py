from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import AbstractUser
from likes.models import Like,DisLike
# Create your models here.


class User(models.Model):

  username = models.CharField(blank=True, max_length=255)
  email = models.EmailField()
  password = models.CharField(blank=True, max_length=255)

  def __str__(self):
      return self.username


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    likes = GenericRelation(Like)
    dislikes = GenericRelation(DisLike)

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']



