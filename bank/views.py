from django.shortcuts import render
from django.views import View
from .models import Bank_Token
import uuid
from django.core.mail import send_mail
from django.conf import settings

def bankTokenView(request):
    return render(request,'bank/bankhome.html')

class ADBLTokenView(View):
    template_name = 'bank/adbl.html'

    def get(self, request, *args, **kwargs):
        tokens = Bank_Token.objects.filter(bank_name='adbl').order_by('-created_at')
        context = {'tokens': tokens}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        token_number = uuid.uuid4().hex[:6].upper()
        token = Bank_Token.objects.create(bank_name='adbl', token_number=token_number)
        tokens = Bank_Token.objects.filter(bank_name='adbl').order_by('-created_at')
        context = {'tokens': tokens, 'token': token}

        # Send email to the client
        recipient_email = request.POST.get('email')  # Assuming the email is submitted through a form field
        subject = 'Your Bank 1 Token Number'
        message = f"Your token number is: {token_number}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

        return render(request, self.template_name, context)
class NBBTokenView(View):
    template_name = 'bank/nbb.html'

    def get(self, request, *args, **kwargs):
        tokens = Bank_Token.objects.filter(bank_name='nbb').order_by('-created_at')
        context = {'tokens': tokens}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        token_number = uuid.uuid4().hex[:6].upper()
        token = Bank_Token.objects.create(bank_name='nbb', token_number=token_number)
        tokens = Bank_Token.objects.filter(bank_name='nbb').order_by('-created_at')
        context = {'tokens': tokens, 'token': token}

        # Send email to the client
        recipient_email = request.POST.get('email')  # Assuming the email is submitted through a form field
        subject = 'Your Bank 1 Token Number'
        message = f"Your token number is: {token_number}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

        return render(request, self.template_name, context)
class RBBTokenView(View):
    template_name = 'bank/rbb.html'

    def get(self, request, *args, **kwargs):
        tokens = Bank_Token.objects.filter(bank_name='rbb').order_by('-created_at')
        context = {'tokens': tokens}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        token_number = uuid.uuid4().hex[:6].upper()
        token = Bank_Token.objects.create(bank_name='rbb', token_number=token_number)
        tokens = Bank_Token.objects.filter(bank_name='rbb').order_by('-created_at')
        context = {'tokens': tokens, 'token': token}

        # Send email to the client
        recipient_email = request.POST.get('email')  # Assuming the email is submitted through a form field
        subject = 'Your Bank 1 Token Number'
        message = f"Your token number is: {token_number}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

        return render(request, self.template_name, context)

class SBLTokenView(View):
    template_name = 'bank/sbl.html'

    def get(self, request, *args, **kwargs):
        tokens = Bank_Token.objects.filter(bank_name='rbb').order_by('-created_at')
        context = {'tokens': tokens}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        token_number = uuid.uuid4().hex[:6].upper()
        token = Bank_Token.objects.create(bank_name='sbl', token_number=token_number)
        tokens = Bank_Token.objects.filter(bank_name='sbl').order_by('-created_at')
        context = {'tokens': tokens, 'token': token}

        # Send email to the client
        recipient_email = request.POST.get('email')  # Assuming the email is submitted through a form field
        subject = 'Your Bank 1 Token Number'
        message = f"Your token number is: {token_number}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

        return render(request, self.template_name, context)
