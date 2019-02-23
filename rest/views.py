from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser 

from rest.models import GalleryImage, GalleryVideo, GalleryAudio, GalleryClipaudio, GalleryClipvideo, GalleryUserlogin, GalleryCategoria
from rest.serializers import ImageSerializer, VideoSerializer, AudioSerializer, ClipAudioSerializer, \
    ClipVideoSerializer, UserLoginSerializer, CategoriaSerializer


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
        clipaudio = GalleryClipaudio.objects.all()
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
        clipaudio = GalleryClipaudio.objects.get(pk=pk)
    except GalleryClipaudio.DoesNotExist:
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
        clipvideo = GalleryClipvideo.objects.all()
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
        clipvideo = GalleryClipvideo.objects.get(pk=pk)
    except GalleryClipvideo.DoesNotExist:
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


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        user = GalleryUserlogin.objects.all()
        serializer = UserLoginSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def login_user(request):
    if request.method == 'GET':
        user = GalleryUserlogin.objects.all()
        serializer = UserLoginSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        usr = request.data.get('login')
        pwd = request.data.get('password')
        print(usr)
        print(usr)
        print(request)
        try:
            user = GalleryUserlogin.objects.get(login=usr)
            if user.password == pwd:
                return Response(UserLoginSerializer(user).data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except GalleryUserlogin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'POST'])
def categoria_list(request):
    if request.method == 'GET':
        categoria = GalleryCategoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail(request, pk):
    try:
        categoria = GalleryCategoria.objects.get(pk=pk)
    except GalleryCategoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)