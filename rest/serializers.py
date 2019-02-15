from .models import GalleryImage, GalleryVideo, GalleryAudio, GalleryClipAudio, GalleryClipVideo
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryImage
      fields = ('name', 'url', 'title', 'author', 'date', 'city', 'country', 'description', 'type', 'imageFile', 'user')


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
      fields = ('name', 'secondStart', 'secondEnd', 'audioName')


class ClipVideoSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryClipVideo
      fields = ('name', 'secondStart', 'secondEnd', 'audioName')