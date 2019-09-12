from .models import Post,User
from django.contrib.auth.models import User as Sys_user
from .serializers import PostSerializer,UserSerializer,SysUserSerializer
from rest_framework import viewsets
from likes.maxins import LikedMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view



class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)



class UserCreateView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view(['GET', 'POST'])
def get_post_users(request):
        # get all
        if request.method == 'GET':
            user = Sys_user.objects.all()
            serializer = SysUserSerializer(user, many=True)
            return Response(serializer.data)
        # insert a new record for a
        elif request.method == 'POST':
            return Response({})

