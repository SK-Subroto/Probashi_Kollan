from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MeetingSerializer, NoticeSerializer
from .models import Notice, Meeting
from users.models import Attendant, Immigrant


def notice(request):
    notices = Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'desk/notice.html', context)


def noticeAttendant(request):
    return render(request, 'desk/noticeAttendant.html')


@api_view(['GET'])
def noticeList(request):
    notices = Notice.objects.all().order_by('-id')
    serializer = NoticeSerializer(notices, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def noticeCreate(request):
    attendant_user_id = Attendant.objects.get(user__id=request.user.id).id
    print(attendant_user_id)
    notice_data = request.data
    print(notice_data)
    new_notice = Notice.objects.create(author=Attendant.objects.get(id=attendant_user_id), title=notice_data["title"],
                                       description=notice_data["description"])
    new_notice.save()
    serializer = NoticeSerializer(new_notice)
    # serializer = NoticeSerializer(data=request.data)

    # if serializer.is_valid():
    #     serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def noticeUpdate(request, pk):
    task = Notice.objects.get(id=pk)
    serializer = NoticeSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Notice.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')


def meeting(request):
    return render(request, 'desk/meeting.html')


@api_view(['GET'])
def meetingList(request):
    meetings = Meeting.objects.all()
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


def meetingAttendant(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if not query:
            immigrant_lists = None
        else:
            immigrant_lists = Immigrant.objects.filter(Q(immigrant_id__icontains=query) |
                                                       Q(immigrant_name__icontains=query) |
                                                       Q(passport_nb__icontains=query))
        # print(immigrant_lists)
        context = {'immigrant_lists': immigrant_lists}
    return render(request, 'desk/meetingAttendant.html', context)


immi_id = 0


@api_view(['POST'])
def getImmigrantId(request):
    immigrant_data = request.data
    global immi_id
    immi_id = immigrant_data["id"]
    return HttpResponse(immi_id)


@api_view(['GET'])
def meetingAttenList(request):
    global immi_id
    print(immi_id)
    meetings = Meeting.objects.filter(immigrant__id=immi_id).order_by('-meeting_date')
    # if immi_id is not 0:
    #     immi_id = 0
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def meetingCreate(request):
    attendant_user_id = Attendant.objects.get(user__id=request.user.id).id
    print(attendant_user_id)
    meeting_data = request.data
    print(meeting_data)
    new_notice = Meeting.objects.create(attendant=Attendant.objects.get(id=attendant_user_id),
                                        immigrant=Immigrant.objects.get(id=1),
                                        title=meeting_data["title"],
                                        description=meeting_data["description"],
                                        meeting_date=meeting_data["meeting_date"])
    new_notice.save()
    serializer = MeetingSerializer(new_notice)
    # serializer = NoticeSerializer(data=request.data)

    # if serializer.is_valid():
    #     serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def meetingUpdate(request, pk):
    task = Meeting.objects.get(id=pk)
    serializer = MeetingSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def meetingDelete(request, pk):
    task = Meeting.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')
