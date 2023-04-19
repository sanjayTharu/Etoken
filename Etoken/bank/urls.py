from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet,BankTokenViewSet,UserRegistrationView,UserLoginView


router=DefaultRouter()
router.register('customers',CustomerViewSet,basename='customers')
router.register('banktoken',BankTokenViewSet,basename='banktoken')

urlpatterns=[
    path('',include(router.urls)),
    path('register/',UserRegistrationView.as_view(),name='user_registration'),
    path('login/',UserLoginView.as_view(),name='user_login'),
]
