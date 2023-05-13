from django.urls import path
from .views import NBBTokenView,RBBTokenView,bankTokenView,ADBLTokenView

app_name = 'your_app_name'

urlpatterns = [
    path('bank/', bankTokenView, name='bankhome'),
    path('bank2/', NBBTokenView.as_view(), name='nbbbank'),
    path('bank3/', RBBTokenView.as_view(), name='rbbbank'),
    path('bank3/', ADBLTokenView.as_view(), name='adblbank'),
]
