from .models import GalleryImage, GalleryVideo, GalleryAudio, GalleryClipaudio, GalleryClipvideo, GalleryUserlogin, GalleryCategoria
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
      model = GalleryClipaudio
      fields = ('name', 'secondstart', 'secondend', 'audioname', 'email')


class ClipVideoSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryClipvideo
      fields = ('name', 'secondstart', 'secondend', 'videoname' , 'email')


class UserLoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
          write_only=True,
    )

    class Meta:
       model = GalleryUserlogin
       fields = ('login', 'password', 'name', 'lastname', 'email', 'photo', 'city', 'country')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryCategoria
      fields = ('id', 'description', 'type')
