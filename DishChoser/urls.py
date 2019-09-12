from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from post import views
from emailsignup import urls

# Регистрируем API

apipatterns = [
   url(r'^', include('post.urls')),
]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apipatterns)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/', include('emailsignup.urls')), # verify from mail
    url(r'auth/users/', views.get_post_users, name='get_post_users'), # print all user !admin only!
    url(r'^auth/registration/', include('rest_auth.registration.urls')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
