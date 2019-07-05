from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

router2 = routers.DefaultRouter()
router2.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router2.urls)),
    path('auth/', ObtainAuthToken.as_view()),
]