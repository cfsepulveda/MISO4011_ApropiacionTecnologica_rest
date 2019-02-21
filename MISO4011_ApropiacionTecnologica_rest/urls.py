from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from rest import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('images/', views.image_list),
    path('videos/', views.video_list),
    path('audios/', views.audio_list),
    path('clipVideo/', views.clipvideo_list),
    path('clipAudio/', views.clipaudio_list),
    path('images/<int:pk>', views.image_detail),
    path('videos/<int:pk>', views.video_detail),
    path('audios/<int:pk>', views.audio_detail),
    path('clipAudio/<int:pk>', views.clipaudio_detail),
    path('clipVideo/<int:pk>', views.clipvideo_detail),
    path('registerUser/', views.user_list),
    path('loginUser/', views.login_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)