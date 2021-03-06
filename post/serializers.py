from rest_framework import serializers

from myapp.models import Student
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {'author': {'required': False}}


