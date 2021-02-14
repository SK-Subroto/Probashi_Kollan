from rest_framework import serializers
from .models import Meeting, Notice
from users.models import Attendant


class MeetingSerializer(serializers.ModelSerializer):
    attendant = serializers.CharField(read_only=True)
    meeting_date = serializers.DateTimeField(read_only=True, format="%m/%d/%Y %I:%M %p")
    date_posted = serializers.DateTimeField(read_only=True, format="%m/%d/%Y %I:%M %p")

    class Meta:
        model = Meeting
        fields = ('id', 'attendant', 'immigrant', 'title', 'description', 'date_posted', 'meeting_date', 'meeting_status')


# class AttendantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendant
#         fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True, format="%d-%m-%Y")
    # date_posted = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    # author = AttendantSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = ('id', 'author', 'title', 'description', 'date_posted')
        # depth = 2

