from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MeetingSerializer, NoticeSerializer
from .models import Notice, Meeting
from .filters import NoticeFilter
from users.models import Attendant, Immigrant, Country
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def notice(request):
    country_code = Immigrant.objects.get(user__id=request.user.id).region.country_code
    region = Country.objects.get(country_code=country_code)

    notices = Notice.objects.all().order_by('-date_posted')

    filter_data = request.GET.copy()
    filter_data.setdefault('region', region)

    noticeFilter = NoticeFilter(filter_data, queryset=notices)
    notices = noticeFilter.qs

    context = {'notices': notices, 'noticeFilter': noticeFilter}
    return render(request, 'desk/notice.html', context)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def noticeAttendant(request):
    return render(request, 'desk/noticeAttendant.html')


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['GET'])
def noticeList(request):
    notices = Notice.objects.all().order_by('-id')
    serializer = NoticeSerializer(notices, many=True)
    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['POST'])
def noticeCreate(request):
    attendant_user_id = Attendant.objects.get(user__id=request.user.id).id
    print(attendant_user_id)
    notice_data = request.data
    print(notice_data)
    new_notice = Notice.objects.create(author=Attendant.objects.get(id=attendant_user_id),
                                       region=Country.objects.get(country_code=notice_data["region"]),
                                       title=notice_data["title"],
                                       description=notice_data["description"])
    new_notice.save()
    serializer = NoticeSerializer(new_notice)
    # serializer = NoticeSerializer(data=request.data)

    # if serializer.is_valid():
    #     serializer.save()

    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['POST'])
def noticeUpdate(request, pk):
    task = Notice.objects.get(id=pk)
    serializer = NoticeSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Notice.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def meeting(request):
    return render(request, 'desk/meeting.html')


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
@api_view(['GET'])
def meetingList(request):
    meetings = Meeting.objects.filter(Q(immigrant__user_id=request.user.id) & Q(meeting_status=True)).order_by('-date_posted')
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
@api_view(['POST'])
def meetingImmiCreate(request):
    user_id = request.user.id
    print(user_id)
    meeting_data = request.data
    print(meeting_data)
    new_notice = Meeting.objects.create(immigrant=Immigrant.objects.get(user_id=user_id),
                                        title=meeting_data["title"],
                                        description=meeting_data["description"])
    new_notice.save()
    serializer = MeetingSerializer(new_notice)

    return Response(serializer.data)


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
@api_view(['GET'])
def meetingPendingList(request):
    meetings = Meeting.objects.filter(Q(immigrant__user_id=request.user.id) & Q(meeting_status=False))
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def meetingAttendant(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if not query:
            immigrant_lists = None
        else:
            immigrant_lists = Immigrant.objects.filter(Q(immigrant_id__icontains=query) |
                                                       Q(user__first_name__icontains=query) |
                                                       Q(passport_nb__icontains=query))
        # print(immigrant_lists)
        context = {'immigrant_lists': immigrant_lists}
    return render(request, 'desk/meetingAttendant.html', context)


immi_id = 0


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['POST'])
def getImmigrantId(request):
    immigrant_data = request.data
    global immi_id
    immi_id = immigrant_data["id"]
    return HttpResponse(immi_id)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['GET'])
def meetingAttenList(request):
    global immi_id
    print(immi_id)
    meetings = Meeting.objects.filter(immigrant__id=immi_id).order_by('-meeting_date')
    # if immi_id is not 0:
    #     immi_id = 0
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
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


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['POST'])
def meetingUpdate(request, pk):
    task = Meeting.objects.get(id=pk)
    serializer = MeetingSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print('error')

    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['DELETE'])
def meetingDelete(request, pk):
    task = Meeting.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['GET'])
def meetingAttenPendingList(request):
    meetings = Meeting.objects.filter(meeting_status=False).order_by('-meeting_date')
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['POST'])
def meetingAttenPendingUpdate(request, pk):
    attendant_user_id = Attendant.objects.get(user__id=request.user.id).id
    meeting = Meeting.objects.get(id=pk)
    meeting.attendant = Attendant.objects.get(id=attendant_user_id)
    meeting.meeting_date = request.data["meeting_date"]
    print(request.data["meeting_date"])
    print(meeting)
    serializer = MeetingSerializer(instance=meeting, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print('error')

    return Response(serializer.data)