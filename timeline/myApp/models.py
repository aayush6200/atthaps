from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255) 
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()

    def __str__(self):
        return self.title +'|'+str(self.author)

class Language(models.Model):
    language=models.CharField(max_length=255)
    body=models.TextField()
    



