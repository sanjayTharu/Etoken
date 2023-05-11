from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BankTokenView,generate_token


app_name='bank'

urlpatterns=[
    path('generate-token/',generate_token,name='bank_token'),
    path('dashboard/',BankTokenView.as_view(),name='dashboard'),
   
]
