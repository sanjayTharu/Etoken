from rest_framework import generics,status,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Office_Token
from .serializers import OfficeTokenSerializer
import uuid
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Office_Token
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
def generate_office_token(request):
    if request.method=='POST':
        office_name=request.data.get('office_name')
        if office_name:
            token_number=uuid.uuid4().hex[:6].upper()
            token=Office_Token.objects.create(office_name=office_name,token_number=token_number)
            #sending mail to the client
            subject="Token Generated"
            message=f"Your token number is:{token.token_number}"
            from_email='your_email@example.com'
            recipient_list=User.objects.values.values.list('email',flat=True)
            send_mail(subject,message,from_email,recipient_list)
            return Response({'token_number':token.token_number},template_name='office/token.html')
        else:
            return Response({'error':'Office  name is required'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return redirect('/officehome/')
class OffcieTokenView(View):
    template_name='office/dashboard.html'

    def get(self,request,*args,**kwargs):
        tokens=Office_Token.objects.all().order_by('-created_at')
        context={'tokens':tokens}
        return render(request,self.template_name,context)
    
    def post(self,request,*args,**kwargs):
        office_name=request.POST.get('office_name')
        if office_name:
            token_number=uuid.uuid4().hex[:6].upper()
            token=Office_Token.objects.create(office_name=office_name,token_number=token_number)
            tokens=Office_Token.objects.all().order_by('-created_at')
            context={'tokens':tokens,'token':token}
            return render(request,self.template_name,context)
        else:
            return Response({'error':'Office name is required'},status=status.HTTP_400_BAD_REQUEST)
