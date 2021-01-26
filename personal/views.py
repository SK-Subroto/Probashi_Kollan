from django.shortcuts import render
from django.http import HttpResponse


def passport(request):
    return HttpResponse("this is passport")


def visa(request):
    return HttpResponse("this is visa")


def report(request):
    return HttpResponse("this is report")


def moneyTransfer(request):
    return HttpResponse("this is moneyTransfer")


def doctor(request):
    return render(request, 'personal/doctor.html')


def lawyer(request):
    return render(request, 'personal/lawyer.html')