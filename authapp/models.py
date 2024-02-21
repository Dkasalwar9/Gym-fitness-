
# from django.db import models

# # Create your models here.

# class Contact(models.Model):
#     name=models.CharField(max_length=25)
#     email=models.CharField(max_length=12)
#     phonenumber=models.CharField(max_length=12)
#     description=models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.email
    
# class Enrollment(models.Model):
#     FullName=models.CharField(max_length=25)
#     Email=models.CharField(max_length=25)
#     Gender=models.CharField(max_length=25)
#     PhoneNumber=models.CharField(max_length=12)
#     DOB=models.CharField(max_length=55)
#     SelectMembership=models.CharField(max_length=25)
#     # SelectMembership = models.CharField(max_length=50, default='default_value')
#     SelectTrainer=models.CharField(max_length=55)
#     Reference=models.CharField(max_length=55)
#     Address=models.TextField()
#     paymentStatus=models.CharField(max_length=55,blank=True,null=True)
#     price=models.IntegerField(max_length=55,blank=True,null=True)
#     DueDate=models.DateTimeField(blank=True,null=True)
#     timestamp=models.DateTimeField(auto_now_add=True,blank=True)

#     def __str__(self):
#         return self.FullName


# class Trainer(models.Model):
#     name=models.CharField(max_length=25)
#     gender=models.CharField(max_length=25)
#     phone=models.CharField(max_length=25)
#     salary=models.IntegerField()
#     timestamp=models.DateTimeField(auto_now_add=True,blank=True)



#     def __str__(self):
#         return self.name



# class MembershipPlan(models.Model):
#     plan=models.CharField(max_length=155)
#     price=models.IntegerField(max_length=155)

#     def __int__(self):
#         return self.plan

from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=12)
    phonenumber=models.CharField(max_length=12)
    description=models.TextField(null=True)

    def _str_(self):
        return self.email
    

class Enrollment(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    SelectMembershipplan=models.CharField(max_length=50, null=True)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55, null=True)
    Address=models.CharField(max_length=255, null=True)
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    DueDate=models.DateTimeField(null=True, blank=True)
    # timeStamp=models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.FullName
    
class Trainer(models.Model):
    name=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField()
    # timeStamp=models.DateTimeField(blank=True)
    timeStamp = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)

    def _int_(self):
        return self.id
    
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    # timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    timeStamp = models.DateTimeField(default=timezone.now)
    def __int__(self):
        return self.id
    
class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15, default='your_default_value_here')
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200, null=True)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    
    def __int__(self):
        return self.id