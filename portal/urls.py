from django.urls import path
from . import views

urlpatterns = [
    path('job/', views.job),
    path('blog/', views.blog),
    path('flight/', views.flight),
    path('chat/', views.chat),
]