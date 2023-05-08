from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import render,redirect
from .models import Customer,Bank_Token
from .serializers import CustomerSerializer,BankTokenSerializer,UserSerializer,LoginSerializer
from django.views.generic.edit import CreateView
import uuid
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Bank_Token
from django.views import View


# Create your views here.

@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
def generate__token(request):
    bank_name=request.data.get('bank_name')
    if bank_name:
        token_number=uuid.uuid4().hex[:6].upper()
        token=Bank_Token.objects.create(bank_name=bank_name,token_number=token_number)
        return Response({'token_number':token.token_number},template_name='token.html')
    else:
        return Response({'error':'Bank  name is required'},status=status.HTTP_400_BAD_REQUEST)
    
class BankTokenView(View):
    template_name='bank/dashboard.html'

    def get(self,request,*args,**kwargs):
        tokens=Bank_Token.objects.all().order_by('-created_at')
        context={'tokens':tokens}
        return render(request,self.template_name,context)
    
    def post(self,request,*args,**kwargs):
        bank_name=request.POST.get('bank_name')
        if bank_name:
            token_number=uuid.uuid4().hex[:6].upper()
            token=Bank_Token.objects.create(bank_name=bank_name,token_number=token_number)
            tokens=Bank_Token.objects.all().order_by('-created_at')
            context={'tokens':tokens,'token':token}
            return render(request,self.template_name,context)
        else:
            return Response({'error':'Bank name is required'},status=status.HTTP_400_BAD_REQUEST)
