
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

