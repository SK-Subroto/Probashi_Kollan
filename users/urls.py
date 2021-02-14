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

    path('profile/', views.profileImmigrant, name='immigrant-profile'),
    path('profile/update', views.profileUpdateImmigrant, name='immigrant-profile-update'),

    path('attendant/profile/', views.profileAttendant, name='attendant-profile'),
    path('attendant/profile/update', views.profileUpdateAttendant, name='attendant-profile-update'),

    path('attendant/search', views.searchImmigrant),
    path('attendant/search/<str:pk>', views.searchImmigrantDetail, name='attendant-search-detail'),
]