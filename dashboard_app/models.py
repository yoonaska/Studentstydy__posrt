from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    discrption = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= "notes"
        verbose_name_plural= "notes"