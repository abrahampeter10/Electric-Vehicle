from django.shortcuts import render,redirect
from . models import*
from django.contrib import messages
from userapp.models import * 

# Create your views here.
def creg(request):
    if request.method=="POST":
        YourName=request.POST.get('YourName')
        email=request.POST.get('email')
        CompanyName=request.POST.get('CompanyName')
        CompanyID=request.POST.get('CompanyID')
        Location=request.POST.get('Location')
        State=request.POST.get('State')
        Image=request.FILES.get('Image')
        PhNumber=request.POST.get('PhNumber')
        Password=request.POST.get('Password')
        ConfirmPassword=request.POST.get('ConfirmPassword')
        
       
        if Password==ConfirmPassword:
            if charging_reg.objects.filter(email=email).exists():
                messages.info(request,'Email Address Already Exists')
            else:
                userdata = charging_reg( YourName= YourName,email=email,CompanyName=CompanyName, CompanyID=CompanyID,Location=Location,State=State,Image=Image,PhNumber=PhNumber,Password=Password)
                userdata.save()
                return redirect('clog')
    return render(request,'chargingstation/creg.html')
def clog(request ):
     error_message=None
     if request.method=="POST":

          try:

              YourName=request.POST.get('YourName')
              Password=request.POST.get('Password')
              log=charging_reg.objects.get(YourName=YourName,Password=Password)
              #if log.accept:
              request.session['YourName']=log.YourName
              request.session['id']=log.id

              return redirect('chome')


          except charging_reg.DoesNotExist as e : 
              messages.info(request, 'Invalid User')
     return render(request,'chargingstation/clog.html')
def chome(request ):
    return render(request,'chargingstation/chome.html')
def booking(request,pk):
    b=chargingslotbooking.objects.filter(cid=pk)
    return render(request,'chargingstation/booking.html',{'b':b})
def add(request ):
     if request.method=='POST':
         Location=request.POST.get('Location')
         Address=request.POST.get('Address')
         Totalconnectors=request.POST.get('Totalconnectors')
         avconnectors=request.POST.get('avconnectors')
         powercapacity=request.POST.get('powercapacity')
         operator=request.POST.get('operator')
         rate=request.POST.get('rate')
         image=request.FILES.get('image')
         cid=request.POST['cid']
         addsave=add_charg(Location=Location,Address=Address,Totalconnectors=Totalconnectors,avconnectors=avconnectors,powercapacity=powercapacity,operator=operator,image=image,rate=rate,cid_id=cid)
         addsave.save()
         return redirect ("chome")
     return render(request,'chargingstation/add.html')
def cprofile(request ):
    cpid = request.session['id']
    cpro=charging_reg.objects.get(id=cpid)
    return render(request,'chargingstation/cprofile.html',{'cp':cpro})
def edit(request,etid ):
    et=charging_reg.objects.get(id=etid)
    if request.method=='POST':
        et.YourName=request.POST.get('YourName')
        et.email=request.POST.get('email')
        et.CompanyName=request.POST.get('CompanyName')
        et.CompanyID=request.POST.get('CompanyID')
        et.Location=request.POST.get('Location')
        et.State=request.POST.get('State')
        et.Image=request.FILES.get('Image')
        et.PhNumber=request.POST.get('PhNumber')
        et.Password=request.POST.get('Password')
        et.save()
        return redirect("cprofile")
    return render(request,'chargingstation/edit.html',{'e':et})
def view(request):
    id=request.session['id']
    vv=add_charg.objects.filter(cid=id)
    return render(request,'chargingstation/view.html',{'v':vv})
def select(request,sid ):
    cs=add_charg.objects.get(id=sid)
    return render(request,'chargingstation/select.html',{'cs':cs})

def cdel(request,id):
    cat=add_charg.objects.get(id=id)
    cat.delete()
    return redirect('view')
    
def update(request,tid ):
    up=add_charg.objects.get(id=tid)
    if request.method=='POST':
        up.Name=request.POST.get('Name')
        up.Location=request.POST.get('Location')
        up.Address=request.POST.get('Address')
        up.Totalconnectors=request.POST.get('Totalconnectors')
        up.avconnectors=request.POST.get('avconnectors')
        up.powercapacity=request.POST.get('powercapacity')
        up.operator=request.POST.get('operator')
        up.image=request.FILES.get('image')
        up.save()
        return redirect("view")
    return render(request,'chargingstation/update.html',{'u':up})

def approved(request,id):
    chargingslotbooking.objects.filter(id=id).update(approved=True)
    chargingslotbooking.objects.filter(id=id).update(reject=False)

    return redirect('chome')

def reject(request,id):
    chargingslotbooking.objects.filter(id=id).update(reject=True)
    chargingslotbooking.objects.filter(id=id).update(approved=False)

    return redirect('chome')

