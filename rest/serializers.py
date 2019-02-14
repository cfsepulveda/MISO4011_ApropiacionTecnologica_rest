from .models import GalleryImage
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
      model = GalleryImage
      fields = ('name', 'url')