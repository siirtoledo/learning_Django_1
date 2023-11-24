from django.db import models

# Create your models here.
class Members(models.Model):
    f_name=models.CharField(max_length=25)
    l_name=models.CharField(max_length=25)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=8)
    country=models.CharField(max_length=20,null=True)
