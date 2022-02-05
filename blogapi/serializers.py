from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
import datetime
from blog.models import *

class Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')



class AlbumSerializer(serializers.ModelSerializer):
    tracks1 = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks1']


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields=("__all__")



class ProducSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields=("__all__")

class pro_categorySerializer(serializers.ModelSerializer):
    product_category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product_Categories
        fields = ('__all__')


class albumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields=("__all__")


class MusicianSerializer(serializers.ModelSerializer):
    album_name = serializers.StringRelatedField(many=True)

    class Meta:
        model = Musician
        fields = ('__all__')