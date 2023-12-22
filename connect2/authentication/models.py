from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=50,null=False)
    lastname=models.CharField(max_length=50,null=False)
    gender=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    password = models.CharField(max_length=50)

     