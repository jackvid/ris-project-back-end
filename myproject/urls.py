from django.contrib import admin
from django.urls import path, include
from .api import router
from user import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(urls))
]
