from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog


def job(request):
    return HttpResponse("this is job post")


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'portal/blog.html', context)


def flight(request):
    return HttpResponse("this is job flight")


def chat(request):
    return HttpResponse("this is job chat")
