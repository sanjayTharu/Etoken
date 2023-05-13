from django.shortcuts import render,redirect
from rest_framework import generics,status,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import HospitalTokenSerializer
import uuid
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Hospital_Token
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
def generate_hospital_token(request):
    if request.method=='POST':
        hospital_name=request.data.get('hospital_name')
        if hospital_name:
            token_number=uuid.uuid4().hex[:6].upper()
            token=Hospital_Token.objects.create(hospital_name=hospital_name,token_number=token_number)
                #sending mail to the client
            subject="Token Generated"
            message=f"Your token number is:{token.token_number}"
            from_email='your_email@example.com'
            recipient_list=User.objects.values.values.list('email',flat=True)
            send_mail(subject,message,from_email,recipient_list)
            return Response({'token_number':token.token_number},template_name='hospital/hospitalhome.html')
        else:
            return Response({'error':'Hospital  name is required'},status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return redirect('/hospital_token/')
    
class HospitalTokenView(View):
    template_name='hospital/hospitalhome.html'

    def get(self,request,*args,**kwargs):
        tokens=Hospital_Token.objects.all().order_by('-created_at')
        context={'tokens':tokens}
        return render(request,self.template_name,context)
    
    def post(self,request,*args,**kwargs):
        hospital_name=request.POST.get('hospital_name')
        if hospital_name:
            token_number=uuid.uuid4().hex[:6].upper()
            token=Hospital_Token.objects.create(bank_name=hospital_name,token_number=token_number)
            tokens=Hospital_Token.objects.all().order_by('-created_at')
            context={'tokens':tokens,'token':token}
            return render(request,self.template_name,context)
        else:
            return Response({'error':'Hospital name is required'},status=status.HTTP_400_BAD_REQUEST)


def bharatpurHospital(request):
    return render(request,'hospital/bharatpur.html')

def bpkoiralaHospital(request):
    return render(request,'hospital/bpkoirala.html')