from django.db import models

# Create your models here.
class Appointments(models.Model):
    name= models.CharField(max_length=255)
    age= models.IntegerField()
    gender= models.CharField(max_length=5)
    title= models.CharField(max_length=255)
    start= models.CharField(max_length=255)
    end= models.CharField(max_length=255)
    status= models.CharField(max_length=255, default="open")
