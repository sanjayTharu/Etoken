"""
URL configuration for Etoken project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views as v1
from bank import views as v2

urlpatterns = [
    path('', v1.index,name='index'),
    path('about/', v1.about,name='about'),
    path('contact/', v1.contact,name='contact'),
    path('bank/bank/',v2.bankTokenView,name='bankhome'),
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('banktokens/',include('bank.urls'),name='bankhomepage'),
    path('hospitaltokens/',include('hospital.urls'),name='hospitalpage'),
    path('office_tokens/',include('office.urls')),
]
