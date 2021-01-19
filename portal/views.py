from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from .serializers import BlogSerializer, JobSerializer
from .models import Blog, Job
from users.models import Attendant
from django.contrib.auth.models import User


def job(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'portal/job.html', context)


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'portal/blog.html', context)


def flight(request):
    return render(request, 'portal/flight.html')


def chat(request):
    return HttpResponse("this is job chat")


def blogAttendant(request):
    return render(request, 'portal/blogAttendant.html')


search_q = ''


@api_view(['POST'])
def blogAttenSearch(request):
    query_data = request.data
    search = query_data["search"]
    global search_q
    search_q = search
    print(search)
    return HttpResponse(search)


@api_view(['GET'])
def blogAttenList(request):
    global search_q
    print(search_q)
    if not search_q:
        blogs = Blog.objects.all().order_by('-date_posted')
    else:
        blogs = Blog.objects.filter(Q(title__icontains=search_q)).order_by('-date_posted')
        search_q = ''
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


# @parser_classes([MultiPartParser, FormParser])
@api_view(['POST'])
def blogAttenCreate(request):
    user_id = User.objects.get(id=request.user.id)
    print(user_id)
    blog_data = request.data
    # photo_data = request.FILES["blogFile"]
    new_blog = Blog.objects.create(author=user_id,
                                   title=blog_data["title"],
                                   content=blog_data["content"]
                                   )
    new_blog.save()
    serializer = BlogSerializer(new_blog)

    return Response(serializer.data)


@api_view(['POST'])
def blogUpdate(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def blogDelete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()

    return Response('Item succsesfully delete!')


def attendnatChat(request):
    return render(request, 'portal/chatAttendant.html')


def jobAttendant(request):
    return render(request, 'portal/jobAttendant.html')


@api_view(['POST'])
def jobCreate(request):
    attendant_user = Attendant.objects.get(user__id=request.user.id)
    print(attendant_user)
    job_data = request.data
    print(job_data)
    new_job = Job.objects.create(attendant=attendant_user,
                                 title=job_data["title"],
                                 company_name=job_data["c_name"],
                                 company_logo=job_data["c_logo"],
                                 deadline=job_data["deadline"],
                                 requirements=job_data["requirement"]
                                 )
    new_job.save()
    serializer = JobSerializer(new_job)
    # serializer = NoticeSerializer(data=request.data)

    # if serializer.is_valid():
    #     serializer.save()

    return Response(serializer.data)