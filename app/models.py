from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SigninData(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    #username = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    phonenum = models.IntegerField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + '' +self.lastname
    

    
