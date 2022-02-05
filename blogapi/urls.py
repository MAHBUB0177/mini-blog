from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('PostAPIView',PostAPIView.as_view(),name='PostAPIView'),
    path('CreateAPIView',CreateAPIView.as_view(),name='CreateAPIView'),
    path('RetriveAPIView/<int:pk>/',RetriveAPIView.as_view(),name='RetriveAPIView'),
    path('TrackApiviews',TrackApiview.as_view(),name='TrackApiviews'),
    path('AlbumApiviews',AlbumApiview.as_view(),name='AlbumApiviews'),

    path('ProducSerializerApiViews',ProducSerializerApiView.as_view(),name='ProducSerializerApiViews'),
    path('pro_categorySerializerApiViews',pro_categorySerializerApiView.as_view(),name='pro_categorySerializerApiViews'),
    path('albumsSerializerApiViews',albumsSerializerApiView.as_view(),name='albumsSerializerApiViews'),
    path('MusicianSerializerApiViews',MusicianSerializerApiView.as_view(),name='MusicianSerializerApiViews'),
   
   
    
    
]