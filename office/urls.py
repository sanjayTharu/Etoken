from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import generate_office_token,OffcieTokenView

app_name='office'

urlpatterns=[
    path('generate-token/',generate_office_token,name='office_token'),
    path('dashboard/',OffcieTokenView.as_view(),name='office_dashboard'),

]