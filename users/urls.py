from django.urls import path
from . import views

urlpatterns = [
    path('immigrant/', views.home),
    path('attendant/', views.home_2),
]