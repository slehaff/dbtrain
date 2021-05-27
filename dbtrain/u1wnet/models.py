from django.db import models
from django.urls import reverse

# Create your models here.

class Un1models(models.Model):

    path=models.FilePathField(path ="/home/images",
              match ="u1models.*", 
              recursive = True)
    name=models.CharField(max_length=128)
    version=models.CharField(max_length=128)
    trdata=models.FilePathField(path ="/home/images",
              match ="train.*", 
              recursive = True)
    datecreated=models.DateTimeField(auto_created=True, blank=True)
    dateupdated=models.DateTimeField(auto_now_add=True, blank=True)
    hyperparams= models.TextField()