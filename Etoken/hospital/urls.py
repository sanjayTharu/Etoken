from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet,HospitalTokenViewSet,UserRegistrationView,UserLoginView

router=DefaultRouter()
router.register('patient',PatientViewSet,basename='patient')
router.register('hospitaltoken',HospitalTokenViewSet,basename='hospitaltoken')

urlpatterns=[
    path('',include(router.urls)),
    path('register/',UserRegistrationView.as_view(),name='user-registration'),
    path('login/',UserLoginView.as_view(),name='user-login'),
]