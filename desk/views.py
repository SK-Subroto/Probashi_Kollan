from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MeetingSerializer
from . models import Notice, Meeting


def notice(request):
    notices = Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'desk/notice.html', context)


def meeting(request):
    return render(request, 'desk/meeting.html')


@api_view(['GET'])
def meetingList(request):
    meetings = Meeting.objects.all()
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)