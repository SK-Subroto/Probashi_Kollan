from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ImmigrantForm, ImmigrantUpdateForm, AttendantUpdateForm
from .models import Immigrant, Attendant
from desk.models import Meeting
from portal.models import Blog
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImmigrantSerializer, UserSerializer
from django.core.mail import send_mail
from django.conf import settings


@unauthenticated_user
def landing(request):
    return render(request, 'users/landing.html')


def about(request):
    return render(request, 'users/about.html')


def contact(request):
    return render(request, 'users/contact.html')


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def home(request):
    blogs = Blog.objects.filter(author_id=request.user.id)
    total_blog = blogs.count()

    context = {'total_blog': total_blog}
    return render(request, 'users/immigrant_dashboard.html', context)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def home_2(request):
    immigrants = Immigrant.objects.filter(user__is_active=False).order_by('-user__date_joined')
    total_immigrant = immigrants.count()

    meetings = Meeting.objects.filter(meeting_status=False).order_by('-date_posted')
    total_meeting = meetings.count()

    blogs = Blog.objects.filter(permission=False).order_by('date_posted')
    total_blog = blogs.count()

    context = {'immigrants': immigrants, 'total_immigrant': total_immigrant, 'meetings': meetings, 'total_meeting': total_meeting, 'blogs': blogs, 'total_blog': total_blog}
    return render(request, 'users/attendant_dashboard.html', context)


@unauthenticated_user
def registerImmigrant(request):
    u_form = CreateUserForm()
    i_form = ImmigrantForm()

    if request.method == 'POST':
        u_form = CreateUserForm(request.POST)
        i_form = ImmigrantForm(request.POST)
        if u_form.is_valid() and i_form.is_valid():
            user_im = u_form.save()
            user_im.is_active = False
            user_im.save()

            group = Group.objects.get(name='immigrant')
            user_im.groups.add(group)
            # i_form.save()
            user = u_form.cleaned_data.get('username')
            contact_nb = i_form.cleaned_data.get('contact_nb')
            passport_nb = i_form.cleaned_data.get('passport_nb')

            email = u_form.cleaned_data.get('email')
            first_name = u_form.cleaned_data.get('first_name')

            print(first_name)
            Immigrant.objects.create(
                user=user_im,
                contact_nb=contact_nb,
                passport_nb=passport_nb,
            )

            #send email

            subject = 'PROBASHI KOLLAN'
            message = "Hello " + first_name + ",\nThank you for registering to our site. " \
                                "You can login to your account after get a verification email" + "\n\n"\
                                "Thank you"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)

            messages.success(request, user + ', Your account is pending for verification.')

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


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def profileImmigrant(request):
    immigrant = Immigrant.objects.get(user_id=request.user.id)
    context = {'immigrant': immigrant}
    return render(request, 'users/immigrant_profile.html', context)


@login_required(login_url='login-immigrant')
@allowed_users(allowed_roles=['immigrant'])
def profileUpdateImmigrant(request):
    immigrant = request.user.immigrant
    form = ImmigrantUpdateForm(instance=immigrant)

    if request.method == 'POST':
        form = ImmigrantUpdateForm(request.POST, request.FILES, instance=immigrant)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'users/immigrant_profile_update.html', context)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def profileAttendant(request):
    attendant = Attendant.objects.get(user_id=request.user.id)
    context = {'attendant': attendant}
    return render(request, 'users/attendant_profile.html', context)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def profileUpdateAttendant(request):
    attendant = request.user.attendant
    form = AttendantUpdateForm(instance=attendant)

    if request.method == 'POST':
        form = AttendantUpdateForm(request.POST, request.FILES, instance=attendant)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'users/attendant_profile_update.html', context)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def searchImmigrant(request):
    key = request.GET.get('key')
    # meeting_data = request.data
    # print(meeting_data["key"])
    immigrants = Immigrant.objects.filter(Q(immigrant_id__icontains=key) |
                                               Q(user__first_name__icontains=key) |
                                               Q(user__last_name__icontains=key) |
                                               Q(passport_nb__icontains=key))
    context = {'immigrants': immigrants}
    return render(request,'users/search_result.html', context)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def searchImmigrantDetail(request, pk):
    immigrant = Immigrant.objects.get(id=pk)
    context = {'immigrant': immigrant}
    return render(request, 'users/search_immigration_detail.html', context)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
def pendingUser(request):
    return render(request, 'users/pending_user_request.html')


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['GET'])
def immigrantPendingList(request):
    immigrants = Immigrant.objects.filter(user__is_active=False).order_by('-user__date_joined')
    serializer = ImmigrantSerializer(immigrants, many=True)
    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['POST'])
def immigrantAttenPendingUpdate(request, pk):
    # attendant_user_id = Attendant.objects.get(user__id=request.user.id).id
    user = User.objects.get(id=pk)
    user.is_active = request.data["is_active"]
    # immigrant.user.is_active = request.data["is_active"]
    # meeting.attendant = Attendant.objects.get(id=attendant_user_id)
    # meeting.meeting_date = request.data["meeting_date"]
    # print(request.data["meeting_date"])
    print(request.data)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

        # send email
        email = user.email
        first_name = user.first_name
        subject = 'PROBASHI KOLLAN'
        message = "Hello " + first_name + ",\nYour account verification is completed. " \
                                          "Now you can login to your account." + "\n\n" \
                                          "Thank you"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

    else:
        print(serializer.errors)

    return Response(serializer.data)


@login_required(login_url='login-attendant')
@allowed_users(allowed_roles=['attendant'])
@api_view(['DELETE'])
def immigrantAttenPendingDelete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    # send email
    email = user.email
    first_name = user.first_name
    subject = 'PROBASHI KOLLAN'
    message = "Hello " + first_name + ",\nYour account verification is failed. " \
                                      "Please contact with us for further instruction." + "\n\n" \
                                      "Thank you"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)

    return Response('User successfully delete!')