
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest import views

from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'images', views.ImageViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]
