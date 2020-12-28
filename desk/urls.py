from django.urls import path
from . import views

urlpatterns = [
    path('notice/', views.notice),
    path('meeting/', views.meeting),
    path('meeting-list/', views.meetingList),

]