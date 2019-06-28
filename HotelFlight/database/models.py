import re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Phone = models.PositiveIntegerField()
    Address = models.CharField(max_length=1000)
    Passport_Number = models.CharField(max_length=100, null=True)
    Payment_Info = models.CharField(max_length=100, null=True)


