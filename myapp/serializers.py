from rest_framework import serializers

from myapp.models import Student

import re

from rest_framework.exceptions import ValidationError

from post.models import Post
from post.serializers import PostSerializer


class StudentSerializers(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, read_only=True)

    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post = PostSerializer(write_only=True)

    class Meta:
        model = Student
        fields = '__all__'

    def validate_mobile(self, value):
        mobile_number_pattern = re.compile("^09\d{9}$")
        if mobile_number_pattern.match(value):
            return value

        raise ValidationError('your mobile number is not correct')

    def create(self, validated_data):
        post = validated_data.pop('post')
        student = Student.objects.create(**validated_data)
        my_post = Post.objects.create(**post, author=student)
        return student
