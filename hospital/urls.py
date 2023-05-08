from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import generate_hospital_token,HospitalTokenView

app_name='hospital'

urlpatterns=[
    path('generate-token/',generate_hospital_token,name='hospital_token'),
    path('dashboard/',HospitalTokenView.as_view(),name='hospital_dashboard'),

]