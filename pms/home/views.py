from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home\index.html')

def login(request):
    return render(request,'home\sign.html')

def register(request):
    return render(request,'home\sign.html')
