from .models import GalleryImage, GalleryVideo, GalleryAudio, GalleryClipAudio, GalleryClipVideo, GalleryUserLogin, GalleryCategoria
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryImage
      fields = ('name', 'url', 'title', 'author', 'date', 'city', 'country', 'description', 'type', 'user')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryVideo
      fields = ('name', 'url', 'name', 'url', 'title', 'author', 'date', 'city', 'country')


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryAudio
      fields = ('name', 'url', 'name', 'url', 'title', 'author', 'date', 'city', 'country')

class ClipAudioSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryClipAudio
      fields = ('name', 'secondStart', 'secondEnd', 'audioName', 'email')


class ClipVideoSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryClipVideo
      fields = ('name', 'secondStart', 'secondEnd', 'videoName' , 'email')


class UserLoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
          write_only=True,
    )

    class Meta:
       model = GalleryUserLogin
       fields = ('login', 'password', 'name', 'lastname', 'email', 'photo', 'city', 'country')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryCategoria
      fields = ('id', 'description', 'type')
