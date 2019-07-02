import re
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Phone = models.PositiveIntegerField()
    Address = models.CharField(max_length=1000)
    Passport_Number = models.CharField(max_length=100, null=True)
    Payment_Info = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username


class Hotel(models.Model):
    Hotel_Name = models.CharField(max_length=200)
    Hotel_Location = models.CharField(max_length=500)
    Hotel_Country = models.CharField(max_length=500, null=True)
    TotalSentMoney = models.DecimalField(max_digits=20, decimal_places=2)
    Percentage = models.DecimalField(max_digits=3, decimal_places=2)
    CompanyAdmin = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Description = models.TextField(null=True)

    def __str__(self):
        return self.Hotel_Name


class Room(models.Model):
    SingleBedCount = models.DecimalField(max_digits=1, decimal_places=0)
    DoubleBedCount = models.DecimalField(max_digits=1, decimal_places=0)
    RoomType = models.CharField(max_length=100)
    AirConditioner = models.BooleanField()

    def __str__(self):
        return self.RoomType


class Hotel_Room(models.Model):
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=20, decimal_places=2)
    Complimentary_Breakfast = models.BooleanField()
    Wifi = models.BooleanField()
    Checkin_Date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    Checkout_Date = models.DateField(auto_now=False, auto_now_add=False, null=True)
