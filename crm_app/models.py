from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Agent"),(3,"Customer"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)



class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.admin.username
    


class Agent(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    # fcm_token=models.TextField(default="")
    objects=models.Manager()
    
    def __str__(self):
        return self.admin.username

class Customer(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    # profile_pic=models.FileField()
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects = models.Manager()

# class Profile(models.Model):
#     user = models.OneToOneField(to=User,on_delete=CASCADE)
#     mobile = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username

class Leads(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    destination = models.CharField(max_length=100)
    no_of_days = models.CharField(max_length=50)
    number_of_people = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    city= models.CharField(max_length=100)
    assign = models.ForeignKey(to=Agent,on_delete=CASCADE,null=True,blank=True)