from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from .serializers import BlogSerializer
from .models import Blog
from django.contrib.auth.models import User


def job(request):
    return render(request, 'portal/job.html')


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
