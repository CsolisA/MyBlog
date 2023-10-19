from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=250)


class Post(models.Model):
    name = models.CharField(max_length=40)
    body = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=250, default='')
    image = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    creation_date = models.DateField(default=datetime.now)


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    creation_date = models.DateField(default=datetime.now)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.image}"
