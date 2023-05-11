from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def register_page(request):
    if request.method =='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('confirm-password')

        print(uname,email,password,password2)
        user=User.objects.filter(username=email)

        if user.exists():
            messages.info(request,'Email already exists')
            return redirect('/register/')
        
        if password != password2:
            messages.info(request,'Password and Confirm password didnot match' )
            return redirect('/register/')
        
        else:
            user=User.objects.create_user(username=email)
            user.set_password()
            user.save()

            messages.info(request,'Account Creates Successfully')

        return redirect('/accounts/login/')
    return render(request,'accounts/register.html')
    

def login_page(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        print(username,password)

        if not User.objects.filter(username=username).exists():
            messages.info(request,'Username doesnot exists')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.info(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')
        
    return render(request,'accounts/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')



def home(request):
    return render(request,'accounts/home.html')
