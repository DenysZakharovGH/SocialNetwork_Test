from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from post.models import Post
from post.serializers import PostSerializer
from . import service
from .serializers import FanSerializer


class LikedMixin:

    @action(detail=True,methods=['POST'])
    def like(self, request, pk=None):
        """Лайкает `obj`.
        прежде чем лайкнуть удалим  дислайк
        """
        obj = self.get_object()
        service.remove_dislike(obj, request.user)
        service.add_like(obj, request.user)
        return Response()

    @action(detail=True,methods=['POST'])
    def unlike(self, request, pk=None):
        """Удаляет лайк с `obj`.
        """
        obj = self.get_object()
        service.remove_like(obj, request.user)
        return Response()
#----------------------------------------------------------------------------------------
    @action(detail=True, methods=['POST'])
    def dislike(self, request, pk=None):
        """Дислайкает `obj`.
        прежде чем дислайснуть удалим лайк
        """
        obj = self.get_object()
        service.remove_like(obj, request.user)
        service.add_dislike(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def undislike(self, request, pk=None):
        """Удаляет дислайк с `obj`.
        """
        obj = self.get_object()
        service.remove_dislike(obj, request.user)
        return Response()


    @action(detail=True,methods=['GET'])
    def fans(self, request, pk=None):
        """Получает всех пользователей, которые лайкнули `obj`.
        """
        obj = self.get_object()
        fans = service.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def haters(self, request, pk=None):
        """Получает всех пользователей, которые дислайкнули `obj`.
        """
        obj = self.get_object()
        haters = service.get_heters(obj)
        serializer = FanSerializer(haters, many=True)
        return Response(serializer.data)

#----------------------------------------------------------------------

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(user)
        return Response(serializer.data)