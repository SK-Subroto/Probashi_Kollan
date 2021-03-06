from django.urls import path
from . import views

urlpatterns = [
    path('notice/', views.notice, name='notice'),
    path('attendant/notice/', views.noticeAttendant, name='attendant-notice'),
    path('api/notice-list/', views.noticeList),
    path('api/notice-create/', views.noticeCreate),
    path('api/notice-update/<str:pk>/', views.noticeUpdate),
    path('api/notice-delete/<str:pk>/', views.taskDelete),

    path('meeting/', views.meeting, name='meeting'),
    path('meeting-list/', views.meetingList),
    path('api/meeting-immi-create/', views.meetingImmiCreate),
    path('api/meeting-pending-list/', views.meetingPendingList),
    path('attendant/meeting/', views.meetingAttendant, name='attendant-meeting'),
    path('api/get-immigrant-id/', views.getImmigrantId),
    path('api/meeting-atten-list/', views.meetingAttenList),
    path('api/meeting-create/', views.meetingCreate),
    path('api/meeting-update/<str:pk>/', views.meetingUpdate),
    path('api/meeting-delete/<str:pk>/', views.meetingDelete),
    path('api/meeting-atten-pending-list/', views.meetingAttenPendingList),
    path('api/meeting-atten-pending-update/<str:pk>/', views.meetingAttenPendingUpdate),

]