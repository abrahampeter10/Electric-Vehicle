from django.db import models
from django.utils import timezone

# Create your models here.
class charging_reg(models.Model):
   YourName=models.CharField(max_length=20)
   email=models.EmailField(max_length=50)
   CompanyName=models.CharField(max_length=30) 
   CompanyID = models.CharField(max_length=30)
   Location = models.CharField(max_length=70)
   State = models.CharField(max_length=30)
   PhNumber = models.CharField(max_length=30)
   Image=models.ImageField(upload_to='profile')
   Password=models.CharField(max_length=10)
   

   def __str__(self):
       return self.YourName

class add_charg(models.Model):
#    Name=models.CharField(max_length=20)
   Location=models.CharField(max_length=50)
   Address=models.CharField(max_length=30) 
   Totalconnectors = models.CharField(max_length=30)
   avconnectors = models.CharField(max_length=70)
   powercapacity = models.CharField(max_length=30)
   operator=models.CharField(max_length=10)
   rate=models.CharField(max_length=10,default=True)
   image=models.ImageField(upload_to='profile',null=True)
   cid=models.ForeignKey(charging_reg,on_delete=models.CASCADE)

   def __str__(self):
       return self.Location
   

