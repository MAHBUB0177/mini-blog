from rest_framework import serializers
import datetime
from blog.models import *

class Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')