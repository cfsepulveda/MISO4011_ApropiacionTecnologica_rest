from django.shortcuts import render
from .models import GalleryImage



from rest_framework import viewsets
from rest.serializers import ImageSerializer

 #Create your views here.


class ImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = ImageSerializer


