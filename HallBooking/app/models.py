from django.db import models

# Create your models here.
class AddStaffs(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=100,null=False,blank=False)
    Department=models.CharField(max_length=100,null=True,blank=False)
    password = models.CharField(max_length=100,null=False,blank=False)


class SearchHall(models.Model):
     Username = models.CharField(max_length=100,null=False,blank=False)
     Hallname = models.CharField(max_length=30)
     Date = models.DateField()
     StartTime = models.CharField(null=True,max_length=10)
     EndTime = models.CharField(null=True,max_length=10)
   

class Hallbook(models.Model):
   Username = models.CharField(max_length=100,null=False,blank=False)
   Department =models.CharField(max_length=50)
   Email= models.EmailField()
   Hallname = models.CharField(max_length=30)
   NumberofAttendees = models.CharField(max_length=30)
   Phone = models.CharField(max_length=30)
   Date = models.DateField()
   NameofEvent =models.CharField(max_length=30)
   StartTime = models.CharField(null=True,max_length=10)
   EndTime = models.CharField(null=True,max_length=10)
   Equipments = models.CharField(max_length=100,null = True) 
   otherRequest= models.CharField(max_length=30)

class Feedback(models.Model):
    Username = models.CharField(max_length=100,null=False)
    Email = models.EmailField()
    Feedback = models.CharField(max_length=500)





