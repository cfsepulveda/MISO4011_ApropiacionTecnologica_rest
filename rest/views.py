from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import GalleryImage, GalleryVideo, GalleryAudio, GalleryClipAudio, GalleryClipVideo, AuthUser
from rest.serializers import ImageSerializer, VideoSerializer, AudioSerializer, ClipAudioSerializer, \
    ClipVideoSerializer, UserSerializer


@api_view(['GET', 'POST'])
def image_list(request):
    if request.method == 'GET':
        image = GalleryImage.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def image_detail(request, pk):
    try:
        image = GalleryImage.objects.get(pk=pk)
    except GalleryImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def video_list(request):
    if request.method == 'GET':
        video = GalleryVideo.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def video_detail(request, pk):
    try:
        video = GalleryVideo.objects.get(pk=pk)
    except GalleryVideo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(video)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def audio_list(request):
    if request.method == 'GET':
        audio = GalleryAudio.objects.all()
        serializer = AudioSerializer(audio, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def audio_detail(request, pk):
    try:
        audio = GalleryAudio.objects.get(pk=pk)
    except GalleryAudio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AudioSerializer(audio)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AudioSerializer(audio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        audio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def clipaudio_list(request):
    if request.method == 'GET':
        clipaudio = GalleryClipAudio.objects.all()
        serializer = ClipAudioSerializer(clipaudio, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClipAudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def clipaudio_detail(request, pk):
    try:
        clipaudio = GalleryClipAudio.objects.get(pk=pk)
    except GalleryClipAudio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClipAudioSerializer(clipaudio)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClipAudioSerializer(clipaudio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clipaudio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def clipvideo_list(request):
    if request.method == 'GET':
        clipvideo = GalleryClipVideo.objects.all()
        serializer = ClipVideoSerializer(clipvideo, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClipVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def clipvideo_detail(request, pk):
    try:
        clipvideo = GalleryClipVideo.objects.get(pk=pk)
    except GalleryClipVideo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClipVideoSerializer(clipvideo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClipVideoSerializer(clipvideo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clipvideo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def auth_user_view(request, format=None):
    content = {
        'username': unicode(request.username),
    }
    return Response(content)
