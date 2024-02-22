from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request,'home2.html')

def signin(request):
    ESFO = SigninDataForm
    EUFO = UserForm
    d = {'ESFO':ESFO , 'EUFO':EUFO}
    if request.method == 'POST':
        DSFO = SigninDataForm(request.POST)
        if DSFO.is_valid():
            DSFO.save()
            return HttpResponse('<center><h1>Thankyou your data successfully submit')

        
    return render(request,'signin.html',d)

def login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        AUO = authenticate(username=un,password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username'] = un
            return HttpResponseRedirect(reverse('home3'))

        
    return render(request,'login.html')

def home3(request):
    return render(request,'home3.html')


