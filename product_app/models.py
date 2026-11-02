from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class product(AbstractUser):
    name=models.CharField(max_length=15)
    desciption=models.TextField(null=True)
    category=models.CharField(max_length=12)
    price= models.DecimalField(max_digits=10,decimal_places=1)
    created_at= models.DateField(auto_now_add=True)