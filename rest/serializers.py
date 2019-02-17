from .models import GalleryImage, GalleryVideo, GalleryAudio, GalleryClipAudio, GalleryClipVideo, AuthUser
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
      fields = ('name', 'secondStart', 'secondEnd', 'videoName')


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
          write_only=True,
    )

    class Meta:
       model = AuthUser
       fields = ('password', 'username', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        if 'password' in validated_data:
              user.set_password(validated_data['password'])
              user.save()
        return user
