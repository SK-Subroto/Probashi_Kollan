from rest_framework import serializers
from .models import Blog, Job


class BlogSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True, format="%m/%d/%Y %I:%M %p")

    class Meta:
        model = Blog
        fields = ('id', 'author', 'title', 'content', 'date_posted', 'photo', 'permission')
        depth = 2


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
