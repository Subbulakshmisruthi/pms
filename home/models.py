from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Projects(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.SET_NULL,blank=True)
    title = models.CharField(max_length=15,null=False,blank=True)
    description = models.TextField(max_length=1000,null=True)
    due = models.DateTimeField(null=True,auto_now_add=False)
    estdue = models.DateTimeField(null=True,auto_now_add=False)

class Tasks(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.SET_NULL,blank=True)
    title = models.CharField(max_length=25,null=False,blank=True)
    is_completed = models.BooleanField(default=False)
