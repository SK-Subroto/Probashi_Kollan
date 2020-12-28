from django.urls import path
from . import views

urlpatterns = [
    path('passport/', views.passport),
    path('visa/', views.visa),
    path('report/', views.report),
    path('money_transfer/', views.moneyTransfer),
]