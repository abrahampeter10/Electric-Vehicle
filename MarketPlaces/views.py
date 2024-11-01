
from django.shortcuts import render, redirect
from .models import *  # Import the User_DB model
from django.contrib import messages
import os
from userapp.models import *  # Import the User_DB model


def MarketReg(request):
    if request.method == "POST":
        username = request.POST.get("username")
        CmpId = request.POST.get("CmpId")
        email = request.POST.get("email")
        CmpName = request.POST.get("CmpName")
        CmpLoc = request.POST.get("CmpLoc")
        CmpState = request.POST.get("CmpState")
        Image=request.FILES.get('Image')
        PhNumber=request.POST.get('PhNumber')
        p1 = request.POST.get("password")
        p2 = request.POST.get("confirmpassword")

        if p1 == p2:
            if COMP_DB.objects.filter(Username=username).exists():
                messages.info(request, 'Username Already Exists')
            else:
                # Create a new User_DB object and save it to the database
                userdata = COMP_DB(Username=username, CmpId=CmpId, Email=email, Password=p1, CmpName=CmpName, CmpLoc=CmpLoc, CmpState=CmpState,Image=Image,PhNumber=PhNumber)
                userdata.save()
                return redirect('Mlogin')
        else:
            messages.info(request, 'Passwords do not match')

    # Return the registration form (Mreg.html) for both GET requests and POST requests with errors.
    return render(request, 'Marketplace/Mreg.html')



def Mlogin(request ):
      if request.method=="POST":
          try:
              Username=request.POST.get("Username")
              Password=request.POST.get("password")
              log=COMP_DB.objects.get(Username=Username,Password=Password)
              request.session['Username']=log.Username
              request.session['id']=log.id
              return redirect('CmpUser')
          except COMP_DB.DoesNotExist as e : 
              messages.info(request, 'Invalid User')
      return render(request,'Marketplace/Mlogin.html')



# Create your views here.
def CmpUser(request ):
     return render(request,'Marketplace/CmpUser.html')
# def Addvehicle(request ):
#      return render(request,'Marketplace/Addvehicle.html')

def MProfile(request ):
    caid = request.session['id']
    capro=COMP_DB.objects.get(id=caid)
    return render(request,'Marketplace/MProfile.html',{'capr':capro})

def Medit(request ):
  me=COMP_DB.objects.get(id=request.session['id'])
  if request.method=="POST":      
            # if len(me.Image)>0:
                # os.remove(me.Image.path)
        me.Username= request.POST['username']
        me.Email = request.POST['email']
        me.CmpName = request.POST['CmpName']
        me.CmpId = request.POST['CmpId']
        me.CmpLoc = request.POST['CmpLoc']
        me.CmpState = request.POST['CmpState']
        me.PhNumber = request.POST['PhNumber']
        me.Image = request.FILES['Image']
        me.Password = request.POST['password']
        
        me.save()
        return redirect('MProfile')
  return render(request,'Marketplace/Medit.html',{'me':me})

def Viewvehicle(request ):
    id=request.session['id']
    hh=C_Category.objects.filter(vid=id)
    return render(request,'Marketplace/Viewvehicle.html',{'h':hh})

def Viewdetails(request,xid ):
    cs=C_Category.objects.get(id=xid)
    return render(request,'Marketplace/Viewdetails.html',{'cs':cs})





from .models import C_Category, COMP_DB  # Import your models

# def Addvehicle(request):
#     if request.method == "POST":
#         VehName = request.POST.get('VehName')
#         VehImage = request.FILES.get('VehImg')
#         VehType = request.POST.get('VehType')
#         VehModel = request.POST.get('VehModel')
#         VehDrive = request.POST.get('VehDrive')
#         VehSeat = request.POST.get('VehSeat')
#         VehBattery = request.POST.get('VehBattery')
#         VehRate = request.POST.get('VehRate')
#         cid = request.POST['cid']

#         # Retrieve the COMP_DB instance
#         try:
#             parent_instance = COMP_DB.objects.get(id=cid)
#         except COMP_DB.DoesNotExist:
#             # Handle the case where the parent instance doesn't exist
#             # You can return an error message or redirect to an error page
#             return render(request, "Marketplace/Addvehicle.html", {"message": "COMP_DB record does not exist."})

#         # Create the C_Category instance with the foreign key reference
#         Cmpsave = C_Category(
#             VehName=VehName,
#             VehImg=VehImage,
#             VehType=VehType,
#             VehModel=VehModel,
#             VehDrive=VehDrive,
#             VehSeat=VehSeat,
#             VehBattery=VehBattery,
#             VehRate=VehRate,
#             CID=parent_instance  # Set the foreign key reference
#         )
#         Cmpsave.save()
#         return redirect("CmpUser")

#     return render(request, "Marketplace/Addvehicle.html")

def Addvehicle(request):
    cd = request.session['id']
    if request.method == "POST":
      VehName=request.POST.get('VehName')
      VehImage = request.FILES.get('VehImg')
      VehType=request.POST.get('VehType')
      VehModel = request.POST.get('VehModel')
      VehDrive=request.POST.get('VehDrive')
      VehSeat=request.POST.get('VehSeat')
      VehBattery=request.POST.get('VehBattery')
      VehRate=request.POST.get('VehRate')
      vid=request.POST['vid']
      Cmpsave=C_Category(VehName=VehName,VehImg=VehImage,VehType=VehType,VehModel=VehModel,VehDrive=VehDrive,
      VehSeat=VehSeat,VehBattery=VehBattery,VehRate=VehRate,vid_id=vid)
      Cmpsave.save()
      return redirect("CmpUser")
    return render(request,"Marketplace/Addvehicle.html",{"cd":cd})

def Mupdate(request,Mid ):
    up=C_Category.objects.get(id=Mid)
    if request.method=='POST':
        up.VehName=request.POST.get('VehName')
        up.VehType=request.POST.get('VehType')
        up.VehModel=request.POST.get('VehModel')
        up.VehDrive=request.POST.get('VehDrive')
        up.VehSeat=request.POST.get('VehSeat')
        up.VehBattery=request.POST.get('VehBattery')
        up.VehRate=request.POST.get('VehRate')
        up.VehImg=request.FILES.get('VehImg')
        up.save()
        return redirect("Viewvehicle")
    return render(request,'Marketplace/Mupdate.html',{'up':up})

def mdel(request,id):
    m=C_Category.objects.get(id=id)
    m.delete()
    return redirect('Viewvehicle')
    

def Mbookings(request,mk ):
    mb=mar_vehicle.objects.filter(vid=mk)
    return render(request,'Marketplace/Mbookings.html',{'mb':mb})

def mapproved(request,id):
    mar_vehicle.objects.filter(id=id).update(approved=True)
    mar_vehicle.objects.filter(id=id).update(reject=False)

    return redirect('CmpUser')

def mreject(request,id):
    mar_vehicle.objects.filter(id=id).update(reject=True)
    mar_vehicle.objects.filter(id=id).update(approved=False)

    return redirect('CmpUser')