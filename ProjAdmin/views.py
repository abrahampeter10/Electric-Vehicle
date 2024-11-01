from django.shortcuts import render,redirect
from chargingstations.models import *
from MarketPlaces.models import *
from userapp.models import *
from .models import *
from django.contrib import messages

# Create your views here.

def plog(request ):
      if request.method=="POST":
          try:
              Email=request.POST.get("email")
              Password=request.POST.get("Password")
              log=adminreg.objects.get(Email=Email,Password=Password)
              request.session['email']=log.Email
              request.session['id']=log.id
              return redirect('Pindex')
          except adminreg.DoesNotExist as e : 
              messages.info(request, 'Invalid Email')
      return render(request,'Project Admin/plog.html')

def Pindex(request ):
    return render(request,'Project Admin/Pindex.html')
def sreg(request ):
    s=charging_reg.objects.all()
    return render(request,'Project Admin/sreg.html',{'s':s})
def slot(request ):
    l=add_charg.objects.all()
    return render(request,'Project Admin/slot.html',{'l':l})
def sbook(request ):
    b=chargingslotbooking.objects.all()
    return render(request,'Project Admin/sbook.html',{'b':b})
def preg(request ):
    p=COMP_DB.objects.all()
    return render(request,'Project Admin/preg.html',{'p':p})
def cadd(request ):
    c=C_Category.objects.all()
    return render(request,'Project Admin/cadd.html',{'c':c})

def mbook(request ):
    k=mar_vehicle.objects.all()
    return render(request,'Project Admin/mbook.html',{'k':k})

def rreg(request ):
    g=User_DB.objects.all()
    return render(request,'Project Admin/rreg.html',{'g':g})

def statbook(request ):
    o=chargingslotbooking.objects.all()
    return render(request,'Project Admin/statbook.html',{'o':o})

def mveh(request ):
    e=mar_vehicle.objects.all()
    return render(request,'Project Admin/mveh.html',{'e':e})


