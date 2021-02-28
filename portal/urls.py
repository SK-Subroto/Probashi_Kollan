from django.urls import path, include
from . import views
# from .router import router
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('test', views.blogAttenCreate,  basename='ln-languages')

urlpatterns = [
    path('job/', views.job, name='job'),
    path('blog/', views.blog, name='blog'),
    path('flight/', views.flight, name='flight'),
    path('chat/', views.chat),

    path('attendant/blog/', views.blogAttendant, name='attendant-blog'),
    path('api/blog-list/', views.blogAttenList),
    path('api/blog-search/', views.blogAttenSearch),
    path('api/blog-create/', views.blogAttenCreate),
    path('api/blog-update/<str:pk>/', views.blogUpdate),
    path('api/blog-delete/<str:pk>/', views.blogDelete),
    path('api/blog-pending-list/', views.blogAttenPendingList),

    path('attendant/chat/', views.attendnatChat, name='attendant-chat'),

    path('attendant/job/', views.jobAttendant, name='attendant-job'),
    # path('api/job-create/', views.jobCreate),
    path('attendant/job-create/', views.jobAttendentCreate, name='attendant-job-create'),

    # path('', include(router.urls)),
]