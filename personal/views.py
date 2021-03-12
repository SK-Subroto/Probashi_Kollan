from django.shortcuts import render
from django.http import HttpResponse
from users.models import Immigrant, Country
from users.filters import ImmigrantFilter
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users
from django.db.models import Q


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


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def searchImmigrant(request):
    country_code = Immigrant.objects.get(user__id=request.user.id).region.country_code
    region = Country.objects.get(country_code=country_code)

    immigrants = Immigrant.objects.filter(Q(user__is_active=True) & ~Q(user__id=request.user.id)).order_by('user__first_name')

    filter_data = request.GET.copy()
    filter_data.setdefault('region', region)

    immigrantFilter = ImmigrantFilter(filter_data, queryset=immigrants)
    immigrants = immigrantFilter.qs

    context = {'immigrants': immigrants, 'immigrantFilter': immigrantFilter}
    return render(request, 'personal/immigrant_search_result.html', context)


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def immigrantDetail(request, pk):
    immigrant = Immigrant.objects.get(id=pk)
    context = {'immigrant': immigrant}
    return render(request, 'personal/immigration_details.html', context)