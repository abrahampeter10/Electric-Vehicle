from django.db import models
from django.utils import timezone
# Create your models here.


class COMP_DB(models.Model):
   Username=models.CharField(max_length=20)
   Email=models.EmailField(max_length=50)
   CmpName =models.CharField(max_length=30) 
   CmpId = models.CharField(max_length=30)
   CmpLoc = models.CharField(max_length=70)
   CmpState = models.CharField(max_length=30)
   PhNumber = models.CharField(max_length=30,default=True)
   Image=models.ImageField(upload_to='profile',default=True)
   Password=models.CharField(max_length=10)


   def __str__(self):
       return self.Username


class C_Category(models.Model):
    VehName = models.CharField(max_length=100)
    VehImg = models.ImageField(upload_to="VehImg")
    VehType = models.CharField(max_length=25, null=True)
    VehModel = models.CharField(max_length=50)
    VehDrive = models.CharField(max_length=50)
    VehSeat = models.CharField(max_length=50)
    VehBattery = models.CharField(max_length=50)
    VehRate = models.CharField(max_length=50)
    vid = models.ForeignKey(COMP_DB, on_delete=models.CASCADE)

    def _str_(self):
       return self.VehName
    

# class vehiclebooking(models.Model):
#      bVehName=models.CharField(max_length=50)
#      bVehType=models.CharField(max_length=50)
#      bVehModel = models.CharField(max_length=50)
#      bVehDrive = models.CharField(max_length=50)
#      bVehSeat = models.CharField(max_length=50)
#      bVehBattery = models.CharField(max_length=50)
#      bVehRate = models.CharField(max_length=50)
#      bVehImg=models.ImageField(upload_to='image',default=True)
#      vid=models.ForeignKey(COMP_DB,on_delete=models.CASCADE)
#     #  sid=models.ForeignKey(User_DB,on_delete=models.CASCADE)
#      status = models.BooleanField(default=False)
#      approved=models.BooleanField(default=False)
#      reject=models.BooleanField(default=False)

   
#      def __str__(self):
#        return self.bVehName
    
# class marketbooking(models.Model):
#       mVehName=models.CharField(max_length=50)
#       mVehType=models.CharField(max_length=50)
#       mVehModel = models.CharField(max_length=50)
#       mVehDrive = models.CharField(max_length=50)
#       mVehSeat = models.CharField(max_length=50)
#       mVehBattery = models.CharField(max_length=50)
#       mVehRate = models.CharField(max_length=50)
#       mVehImg=models.ImageField(upload_to='image',default=True)
#       Date=models.CharField(max_length=14)
#       vid=models.ForeignKey(COMP_DB,on_delete=models.CASCADE)
#       user=models.ForeignKey(User_DB,on_delete=models.CASCADE)
#       status = models.BooleanField(default=False)
#       approved=models.BooleanField(default=False)
#       reject=models.BooleanField(default=False)
#     #   Pay=models.BooleanField(default='False')

   
#       def __str__(self):
#         return self.mVehName
