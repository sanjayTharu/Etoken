from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import generate_hospital_token,HospitalTokenView,bharatpurHospital,bpkoiralaHospital

app_name='hospital'

urlpatterns=[
    path('',generate_hospital_token,name='hospital_token'),
    path('dashboard/',HospitalTokenView.as_view(),name='hospital_dashboard'),
    path('bharatpur/',bharatpurHospital,name='bharatpurhospital'),
    path('bpkoirala/',bpkoiralaHospital,name='bpkoiralahospital'),

]