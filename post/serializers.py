
# serializing post & User data

from .models import Post,User
from django.contrib.auth.models import User as Sys_user
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'body',
            'title',
            'author',
            'total_likes',
            'total_dislikes',
        )



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'password')


class SysUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sys_user
        fields = ('id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',)

