from django.urls import path
from . import views



urlpatterns=[
    path('home/',views.HomeView.as_view(),name='homepage'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('logout/',views.logout_page,name='logout'),
]