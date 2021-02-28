from django.urls import path
from . import views

urlpatterns = [
    path('passport/', views.passport),
    path('visa/', views.visa),
    path('report/', views.report),
    path('money_transfer/', views.moneyTransfer),
    path('emergency/doctor/', views.doctor, name='emergency-doctor'),
    path('emergency/lawyer/', views.lawyer, name='emergency-lawyer'),
    path('find/', views.searchImmigrant, name='find-nearby'),
    path('immigrant/<str:pk>/', views.immigrantDetail, name='immigrant-detail'),
]