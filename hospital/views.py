from django.shortcuts import render
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

# Create your views here.

@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
def generate_hospital_token(request):
    hospital_name=request.data.get('hospital_name')
    if hospital_name:
        token_number=uuid.uuid4().hex[:6].upper()
        token=Hospital_Token.objects.create(hospital_name=hospital_name,token_number=token_number)
        return Response({'token_number':token.token_number},template_name='token.html')
    else:
        return Response({'error':'Hospital  name is required'},status=status.HTTP_400_BAD_REQUEST)
    
class HospitalTokenView(View):
    template_name='hosppital/dashboard.html'

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
