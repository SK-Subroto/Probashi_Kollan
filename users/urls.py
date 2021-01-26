from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('home/', views.home, name='home'),
    path('attendant/home/', views.home_2, name='attendant-home'),

    path('register/', views.registerImmigrant, name='register-immigrant'),
    path('login/', views.loginImmigrant, name='login-immigrant'),

    path('attendant/login/', views.loginAttendant, name='login-attendant'),
    path('logout/', views.logoutUser, name='logout'),
]