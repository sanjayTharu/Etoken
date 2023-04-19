from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CitizenViewSet,OfficeTokenViewSet,UserLoginView,UserRegistrationView

router=DefaultRouter()
router.register('citizens',CitizenViewSet,basename='citizens')
router.register('officetoken',OfficeTokenViewSet,basename='officetoken')


urlpatterns=[
    path('',include(router.urls)),
    path('register/',UserRegistrationView.as_view(),name='userregister'),
    path('login/',UserLoginView.as_view(),name='userlogin'),
]