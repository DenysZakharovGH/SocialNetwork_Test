from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserCreateView


router = DefaultRouter()
router.register(r'post', PostViewSet, basename='user')
router.register(r'users', UserCreateView, basename='account-create'),
urlpatterns = router.urls

