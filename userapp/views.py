from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from chargingstations.models import *
from MarketPlaces.models import *
from evpro.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
global amount
amount=0


# Create your views here.
    
def ureg(request):
    if request.method=="POST":
        username=request.POST.get("username")
        number=request.POST.get("phone") 
        profile=request.FILES.get("profile")
        email=request.POST.get("email")
        p1=request.POST.get("password")
        p2=request.POST.get("confirmpassword")
        if p1==p2:
            if User_DB.objects.filter(Email=email).exists():
                messages.info(request, 'Email Already Exists')
            else:
                userdata=User_DB(Username=username, Number=number,profile=profile,Email=email,Password=p1)
                userdata.save()
                return redirect('ulogin')
        else:
            messages.info(request,'Password not match')
    return render(request,'user/ureg.html')


def ulogin(request):
      if request.method=="POST":
          try:
              Username=request.POST.get("Username")
              Password=request.POST.get("password")
              log=User_DB.objects.get(Username=Username,Password=Password)
              request.session['Username']=log.Username
              request.session['id']=log.id
              return redirect('uhome')
          except User_DB.DoesNotExist as e : 
              messages.info(request, 'Invalid User')
      return render(request,'user/ulogin.html')


def uprofile(request ):
    # caid = request.session['id']
    capro=User_DB.objects.get(id=request.session['id'])
    return render(request,'user/uprofile.html',{'capr':capro})


def ueditprofile(request):
    editp_gen=User_DB.objects.get(id=request.session['id'])
    if request.method=="POST":
        # if len(request.FILES)!=0:
        #     if len(editp_gen.img)>0:
        #         os.remove(editp_gen.img.path)
        editp_gen.Username= request.POST['username']
        editp_gen.Email = request.POST['Email']
        editp_gen.Number=request.POST['Number']
        editp_gen.profile=request.FILES['profile']
        editp_gen.Password = request.POST['Password'] 
        editp_gen.save()
        return redirect('uprofile')
    return render(request, "user/ueditprofile.html",{"editp_gen": editp_gen})


def uhome(request ):
      return render(request,'user/uhome.html')

def orders(request ):
      
    #  id=request.session['id']
    #  try:
    #      data=chargingslotbooking.objects.filter(user=id)
    #  except chargingslotbooking.DoesNotExist as e:

    #      return render(request,'user/orders.html')
     
    id=request.session['id']
    data=chargingslotbooking.objects.filter(user=id,status=False)
    qt=mar_vehicle.objects.filter(user=id,status=False)

    sum=0
    
    for i in data:
         if i.approved:
            sum += int(i.Rate)
            global amount 
            amount=sum

    # sum=0
    
    # for i in qt:
    #      if i.approved:
    #         sum += int(i.VehRate)
    #         global amount 
    #         amount=sum

    

    return render(request,'user/orders.html',{'data':data,'sum':amount,'qt':qt})

   

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def checkout(request):
      global amount
      currency ="INR"
      api_key=RAZORPAY_API_KEY
      amt=int(amount)*100
      payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
      payment_order_id= payment_order['id']  
      chargingslotbooking.objects.filter(user=request.session['id']).update(status=True)
      return render(request,"user/checkout.html",{'a':amount,'api_key':api_key,
      'order_id':payment_order_id})

def stations(request ):
      st=charging_reg.objects.all()
      return render(request,'user/stations.html',{'st':st})

def viewstations(request,vsid ):
    vs=charging_reg.objects.get(id=vsid)
    return render(request,'user/viewstations.html',{'vs':vs})

def Avstations(request,id ):
      av=add_charg.objects.filter(cid=id)
      return render(request,'user/Avstations.html',{'av':av})




def renting(request ):
       rt=COMP_DB.objects.all()
       return render(request,'user/renting.html',{'rt':rt})

def viewvehicle(request,vhid ):
    vh=COMP_DB.objects.get(id=vhid)
    return render(request,'user/viewvehicle.html',{'vh':vh})

def Avehicles(request ,id):
      mv=C_Category.objects.filter(vid=id)
      return render(request,'user/Avehicles.html',{'mv':mv})

def udetails(request,dtid ):
      ud=add_charg.objects.get(id=dtid)
      if request.method=='POST':
         Location=request.POST.get('Location')
         Address=request.POST.get('Address')
         Totalconnectors=request.POST.get('Totalconnectors')
         avconnectors=request.POST.get('avconnectors')
         powercapacity=request.POST.get('powercapacity')
         operator=request.POST.get('operator')
         timeSlot=request.POST.get('timeSlot')
         rate=request.POST.get('rate')
         image=request.FILES.get('image')
         uid=request.session['id']
         cid=request.POST.get('cid')
         add=chargingslotbooking(csLocation=Location,csAddress=Address,Totalconnectors=Totalconnectors,
                         avconnectors=avconnectors,powercapacity=powercapacity,operator=operator,
                         Image=image,timeSlot=timeSlot,Rate=rate,user_id=uid,cid_id=cid)
         add.save()
         return redirect ("uhome")
      return render(request,'user/udetails.html',{'ud':ud})

def vdetails(request,vtid ):
      vd=C_Category.objects.get(id=vtid)
      if request.method=='POST':
         VehName=request.POST.get('VehName')
         VehType=request.POST.get('VehType')
         VehModel=request.POST.get('VehModel')
         VehDrive=request.POST.get('VehDrive')
         VehSeat=request.POST.get('VehSeat')
         VehBattery=request.POST.get('VehBattery')
         VehRate=request.POST.get('VehRate')
         VehImg=request.FILES.get('VehImg')
         Date=request.POST.get('Date')
         uid=request.session['id']
         vid=request.POST.get('vid')
         add=mar_vehicle(VehName=VehName,VehType=VehType,VehModel=VehModel,
                         VehDrive=VehDrive,VehSeat=VehSeat,VehBattery=VehBattery,
                         VehRate=VehRate,VehImg=VehImg,Date=Date,user_id=uid,vid_id=vid)
         add.save()
         return redirect ("uhome")
      return render(request,'user/vdetails.html',{'vd':vd})

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def spay(request, id):
    global amount
    data = chargingslotbooking.objects.get(id=id)
    data.status = True
    data.save()
    amount = data.Rate
    print(amount)
    currency = "INR"
    api_key = RAZORPAY_API_KEY
    amt = int(amount) * 100
    payment_order = client.order.create(dict(amount=amt, currency="INR", payment_capture=1))
    payment_order_id = payment_order['id']
    return render(request, 'user/spay.html', {'a': amount,'d':data, 'api_key': api_key, 'order_id': payment_order_id})

def vpay(request, id):
    global amount
    data = mar_vehicle.objects.get(id=id)
    data.status = True
    data.save()
    amount = data.VehRate
    print(amount)
    currency = "INR"
    api_key = RAZORPAY_API_KEY
    amt = int(amount) * 100
    payment_order = client.order.create(dict(amount=amt, currency="INR", payment_capture=1))
    payment_order_id = payment_order['id']
    return render(request, 'user/vpay.html', {'a': amount,'d':data, 'api_key': api_key, 'order_id': payment_order_id})



def bdetails(request ):
    caid = request.session['id']
    capro=chargingslotbooking.objects.filter(user=caid)
    qt=mar_vehicle.objects.filter(user=caid)
    return render(request,'user/bdetails.html',{'capr':capro,'qt':qt}) 

def cubook(request ,id):
      cv=chargingslotbooking.objects.filter(user=id)
      return render(request,'user/cubook.html',{'cv':cv})




