from django.db import models

# Create your models here.
class Country(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100,primary_key=True)
class Capital(models.Model):
    cpid=models.IntegerField()
    cpname=models.CharField(max_length=100,primary_key=True)
    cname=models.OneToOneField(Country,on_delete=models.CASCADE)
