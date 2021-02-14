from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ImmigrantForm, ImmigrantUpdateForm, AttendantUpdateForm
from .models import Immigrant, Attendant
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users


def landing(request):
    return render(request, 'users/landing.html')


def about(request):
    return render(request, 'users/about.html')


def contact(request):
    return render(request, 'users/contact.html')


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def home(request):
    return render(request, 'users/immigrant_dashboard.html')


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['attendant'])
def home_2(request):
    return render(request, 'users/attendant_dashboard.html')


@unauthenticated_user
def registerImmigrant(request):
    u_form = CreateUserForm()
    i_form = ImmigrantForm()

    if request.method == 'POST':
        u_form = CreateUserForm(request.POST)
        i_form = ImmigrantForm(request.POST)
        if u_form.is_valid() and i_form.is_valid():
            user_im = u_form.save()

            group = Group.objects.get(name='immigrant')
            user_im.groups.add(group)
            # i_form.save()
            user = u_form.cleaned_data.get('username')
            contact_nb = i_form.cleaned_data.get('contact_nb')
            passport_nb = i_form.cleaned_data.get('passport_nb')
            print(user)
            Immigrant.objects.create(
                user=user_im,
                contact_nb=contact_nb,
                passport_nb=passport_nb,
            )
            messages.success(request, 'Account was created for ' + user)

            return redirect('login-immigrant')

    context = {'u_form': u_form, 'i_form': i_form}
    return render(request, 'users/register_Immigrant.html', context)


@unauthenticated_user
def loginImmigrant(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'users/immigrant_login.html', context)


@unauthenticated_user
def loginAttendant(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('attendant-home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'users/attendant_login.html', context)


def logoutUser(request):
    # logout(request)
    if User.objects.filter(pk=request.user.id, groups__name='immigrant').exists() == True:
        logout(request)
        return redirect('login-immigrant')
    elif User.objects.filter(pk=request.user.id, groups__name='attendant').exists() == True:
        logout(request)
        return redirect('login-attendant')
    else:
        logout(request)
        return HttpResponse("Not a part of any group")


def profileImmigrant(request):
    immigrant = Immigrant.objects.get(user_id=request.user.id)
    context = {'immigrant': immigrant}
    return render(request, 'users/immigrant_profile.html', context)


def profileUpdateImmigrant(request):
    immigrant = request.user.immigrant
    form = ImmigrantUpdateForm(instance=immigrant)

    if request.method == 'POST':
        form = ImmigrantUpdateForm(request.POST, request.FILES, instance=immigrant)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'users/immigrant_profile_update.html', context)


def profileAttendant(request):
    attendant = Attendant.objects.get(user_id=request.user.id)
    context = {'attendant': attendant}
    return render(request, 'users/attendant_profile.html', context)


def profileUpdateAttendant(request):
    attendant = request.user.attendant
    form = AttendantUpdateForm(instance=attendant)

    if request.method == 'POST':
        form = AttendantUpdateForm(request.POST, request.FILES, instance=attendant)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'users/attendant_profile_update.html', context)


def searchImmigrant(request):
    key = request.GET.get('key')
    # meeting_data = request.data
    # print(meeting_data["key"])
    immigrants = Immigrant.objects.filter(Q(immigrant_id__icontains=key) |
                                               Q(immigrant_name__icontains=key) |
                                               Q(passport_nb__icontains=key))
    context = {'immigrants': immigrants}
    return render(request,'users/search_result.html', context)


def searchImmigrantDetail(request, pk):
    immigrant = Immigrant.objects.get(id=pk)
    context = {'immigrant': immigrant}
    return render(request, 'users/search_immigration_detail.html', context)