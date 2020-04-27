from django.shortcuts import render,redirect
from  . forms import *
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from .models import *

# Create your views here.
def index1(request):
    return render(request,'index.html/')

def index2(request):
    if request.method == 'POST':
        form =  contactus(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = contactus()
        return render(request,'contactus.html/',{'form':form})

def index3(request):
    return render(request,'aboutus.html/')

def index4(request):
    if request.method == 'POST':
        form = upload1(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/index1.html/')
    else:
        form = upload1()
        return render(request,'uploadpage.html/',{'form':form})

def index5(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'Signin.html/', {'form': form})

def index6(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, 'Your account has been created!')
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Your account has been created!')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request,'SignUp.html',{'form':form})

def index7(request):
    logout(request)
    return redirect('/')




def index9(request):
    return render(request,'termsandconditions.html/')

def index10(request):
    return render(request,'privacyandpolicy.html/')

def index11(request):
    display = upload.objects.all()
    print(display)
    params = {'upload':display}
    return render(request,'index1.html/',params)