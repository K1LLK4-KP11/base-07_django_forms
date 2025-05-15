from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

# Create your models here.
class book(models.Model):  
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=200)  
    description = models.TextField(max_length=500)  
    published_date = models.DateTimeField()  