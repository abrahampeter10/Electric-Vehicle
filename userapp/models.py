from django.db import models
from django.utils import timezone
from chargingstations.models import *
from MarketPlaces.models import*
# Create your models here.
class User_DB(models.Model):
   Username=models.CharField(max_length=20)
   Number=models.CharField(max_length=50)
   Email=models.EmailField(max_length=50)
   profile=models.ImageField(upload_to='profile',default=True)
   Password=models.CharField(max_length=10)
   
   def __str__(self):
       return self.Username
   


class chargingslotbooking(models.Model):
     csLocation=models.CharField(max_length=50)
     csAddress=models.CharField(max_length=50)
     Totalconnectors=models.CharField(max_length=50)
     avconnectors=models.CharField(max_length=50)
     powercapacity=models.CharField(max_length=50)
     operator=models.CharField(max_length=50)
     timeSlot=models.CharField(max_length=50)
     Rate=models.CharField(max_length=50)
     Image=models.ImageField(upload_to='image',default=True)
     cid=models.ForeignKey(charging_reg,on_delete=models.CASCADE)
     user=models.ForeignKey(User_DB,on_delete=models.CASCADE)
    #  vid = models.ForeignKey(COMP_DB, on_delete=models.CASCADE)
     status = models.BooleanField(default=False)
     approved=models.BooleanField(default=False)
     reject=models.BooleanField(default=False)



   
     def __str__(self):
       return self.csLocation
     

# class vehiclebooking(models.Model):
#      VehName=models.CharField(max_length=50)
#      VehType=models.CharField(max_length=50)
#      VehModel = models.CharField(max_length=50)
#      VehDrive = models.CharField(max_length=50)
#      VehSeat = models.CharField(max_length=50)
#      VehBattery = models.CharField(max_length=50)
#      VehRate = models.CharField(max_length=50)
#      VehImg=models.ImageField(upload_to='image',default=True)       
#      Date=models.CharField(max_length=14)
#      vid=models.ForeignKey(COMP_DB,on_delete=models.CASCADE)
#      user=models.ForeignKey(User_DB,on_delete=models.CASCADE)
#      status = models.BooleanField(default=False)
#      approved=models.BooleanField(default=False)
#      reject=models.BooleanField(default=False)
#    # Pay=models.BooleanField(default='False')
     

   
#      def __str__(self):
#        return self.VehName
     
class mar_vehicle(models.Model):
     VehName=models.CharField(max_length=50)
     VehType=models.CharField(max_length=50)
     VehModel = models.CharField(max_length=50)
     VehDrive = models.CharField(max_length=50)
     VehSeat = models.CharField(max_length=50)
     VehBattery = models.CharField(max_length=50)
     VehRate = models.CharField(max_length=50)
     VehImg=models.ImageField(upload_to='image',default=True)       
     Date=models.CharField(max_length=14)
     vid=models.ForeignKey(COMP_DB,on_delete=models.CASCADE)
     user=models.ForeignKey(User_DB,on_delete=models.CASCADE)
     status = models.BooleanField(default=False)
     approved=models.BooleanField(default=False)
     reject=models.BooleanField(default=False)
   # Pay=models.BooleanField(default='False')
     

   
     def __str__(self):
       return self.VehName
       