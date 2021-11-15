from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('PostAPIView',PostAPIView.as_view(),name='PostAPIView'),
    path('CreateAPIView',CreateAPIView.as_view(),name='CreateAPIView'),
    path('RetriveAPIView/<int:pk>/',RetriveAPIView.as_view(),name='RetriveAPIView'),
   
    
    
]