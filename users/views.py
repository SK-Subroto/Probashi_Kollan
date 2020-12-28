from django.shortcuts import render


def home(request):
    return render(request, 'users/immigrant_dashboard.html')
