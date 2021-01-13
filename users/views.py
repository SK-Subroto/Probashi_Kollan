from django.shortcuts import render


def home(request):
    return render(request, 'users/immigrant_dashboard.html')


def home_2(request):
    return render(request, 'users/attendant_dashboard.html')
