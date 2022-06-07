from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home\index.html')

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request,"Username or password is incorrect")
    return render(request,'home\sign.html')

# def login(request):
#     return render(request,'home\sign.html')
def register(request):
    form=CreateUserForm()
    messa=''
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()   
            return redirect('login')       
    return render(request,'home/signup.html',{
            'form':form, 'messa':messa
        })

@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect("login")


