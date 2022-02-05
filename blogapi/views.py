
from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView
from rest_framework import generics
from django.db.models import Case, CharField, Value, When, F, query
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

from blog.models import *


from .serializers import *



class PostAPIView(generics.ListAPIView):
    serializer_class = Post_Serializer
    

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

class CreateAPIView(generics.CreateAPIView):
    serializer_class = Post_Serializer

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


class RetriveAPIView(generics.RetrieveAPIView):
    serializer_class = Post_Serializer

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

class AlbumApiview(generics.ListAPIView):
    serializer_class=AlbumSerializer

    def get_queryset(self):
        queryset=Album.objects.filter().order_by('album_name')
        return queryset


class TrackApiview(generics.ListAPIView):
    serializer_class=TrackSerializer

    def get_queryset(self):
        queryset=Track.objects.filter().order_by('album')
        return queryset


class ProducSerializerApiView(generics.ListAPIView):
    serializer_class=ProducSerializer

    def get_queryset(self):
        queryset=Products.objects.filter().order_by('product_name')
        return queryset


class pro_categorySerializerApiView(generics.ListAPIView):
    serializer_class=pro_categorySerializer
    
    def get_queryset(self):
        queryset=Product_Categories.objects.filter().order_by('categories_name')
        return queryset


class albumsSerializerApiView(generics.ListAPIView):
    serializer_class=albumsSerializer
    
    def get_queryset(self):
        queryset=Albums.objects.filter().order_by('name')
        return queryset


class MusicianSerializerApiView(generics.ListAPIView):
    serializer_class=MusicianSerializer
    
    def get_queryset(self):
        queryset=Musician.objects.filter().order_by('first_name')
        return queryset