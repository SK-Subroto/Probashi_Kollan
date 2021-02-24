from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from .serializers import BlogSerializer, JobSerializer
from .models import Blog, Job, Test
from .forms import TestForm, JobFormAtten, blogForm
from users.models import Attendant
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def job(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'portal/job.html', context)


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def blog(request):
    blogs = Blog.objects.filter(permission=True).order_by('-date_posted')
    blog_form = blogForm()
    if request.method == 'POST':
        blog_form = blogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            update_blog = blog_form.save()
            update_blog.author = request.user
            update_blog.save()
            blog_form = blogForm()
            # redirect('job')
        else:
            print("error")
    context = {'blogs': blogs, 'blog_form': blog_form}
    return render(request, 'portal/blog.html', context)


# def blogCreate(request):
#     blog_form = blogForm()
#     if request.method == 'POST':
#         blog_form = blogForm(request.POST, request.FILES)
#         if blog_form.is_valid():
#             blog_form.save()
#     context = {'blog_form': blog_form}
#     return render(request, 'portal/blog.html', context)


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def flight(request):
    return render(request, 'portal/flight.html')


def chat(request):
    return HttpResponse("this is job chat")


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def blogAttendant(request):
    return render(request, 'portal/blogAttendant.html')


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['GET'])
def blogAttenPendingList(request):
    blogs = Blog.objects.filter(permission=False).order_by('-date_posted')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

search_q = ''


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['POST'])
def blogAttenSearch(request):
    query_data = request.data
    search = query_data["search"]
    global search_q
    search_q = search
    print(search)
    return HttpResponse(search)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['GET'])
def blogAttenList(request):
    global search_q
    print(search_q)
    if not search_q:
        blogs = Blog.objects.filter(permission=True).order_by('-date_posted')
    else:
        blogs = Blog.objects.filter(Q(title__icontains=search_q)).order_by('-date_posted')
        search_q = ''
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


# @parser_classes([MultiPartParser, FormParser])
@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
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


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['POST'])
def blogUpdate(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['DELETE'])
def blogDelete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()

    return Response('Item succsesfully delete!')


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def attendnatChat(request):
    return render(request, 'portal/chatAttendant.html')


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def jobAttendentCreate(request):
    form = JobFormAtten()
    if request.method == 'POST':
        form = JobFormAtten(request.POST)
        if form.is_valid():
            form.save()
            # form.reset()

    context = {'form': form}
    return render(request, 'portal/jobAttenCreate.html', context)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def jobAttendant(request):
    return render(request, 'portal/jobAttendant.html')


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
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


def testView(request):
    tests = Test.objects.all()
    context = {'tests': tests}
    return render(request, 'portal/testView.html', context)


def testCreate(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'portal/testCreate.html', context)