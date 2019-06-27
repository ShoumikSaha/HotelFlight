import re
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Route(models.Model):
	Source   = models.CharField(max_length=200)
	Destination = models.CharField(max_length=200)
	def __str__(self):
		return self.Source


class Company(models.Model):
    Company_Email = models.EmailField(max_length=254)
    Company_Phone = models.PositiveIntegerField()
    Company_Address = models.CharField(max_length=1000)
    Company_Password = models.CharField(max_length=100)


class User(models.Model):
    username_regex = re.compile(r'^[a-zA-Z0-9_]{6,}$')  # ({LETTER}|_)({LETTER}|{DIGIT}|_)*

    Name = models.CharField(max_length=200)
    UserName = models.CharField(max_length=100, validators=[
        RegexValidator(regex=username_regex, message='Please enter a valid prefix')])
    Email = models.EmailField(max_length=254)
    Phone = models.PositiveIntegerField()
    Address = models.CharField(max_length=1000)
    Password = models.CharField(max_length=100)
    Passport_Number = models.CharField(max_length=100)
    Payment_Info = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Air_Company(models.Model):
    AirCompany_Name = models.CharField(max_length=200)
    TotalSentMoney = models.DecimalField(max_digits=20, decimal_places=2)
    Percentage = models.DecimalField(max_digits=3, decimal_places=2)
    CompanyAdmin = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.AirCompany_Name


class Flight(models.Model):
    AirCompany = models.ForeignKey(Air_Company, on_delete=models.CASCADE)

    Airplane_Number = models.CharField(max_length=200)

    def __str__(self):
        return self.Airplane_Number


class Flight_Route(models.Model):
    Route = models.ForeignKey(Route, on_delete=models.CASCADE)
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    Time = models.TimeField(auto_now=False, auto_now_add=False)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Price = models.DecimalField(max_digits=20, decimal_places=2)
    Duration = models.DurationField()


class Room(models.Model):
    SingleBedCount = models.DecimalField(max_digits=1, decimal_places=0)
    DoubleBedCount = models.DecimalField(max_digits=1, decimal_places=0)
    RoomType = models.CharField(max_length=100)
    AirConditioner = models.BooleanField()

    def __str__(self):
        return self.RoomType


class Hotel(models.Model):
    Hotel_Name = models.CharField(max_length=200)
    Hotel_Location = models.CharField(max_length=500)
    TotalSentMoney = models.DecimalField(max_digits=20, decimal_places=2)
    Percentage = models.DecimalField(max_digits=3, decimal_places=2)
    CompanyAdmin = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.Hotel_Name


class Hotel_Room(models.Model):
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=20, decimal_places=2)
    Complimentary_Breakfast = models.BooleanField()
    Wifi = models.BooleanField()
    Checkin_Date = models.DateField(auto_now=False, auto_now_add=False)
    Checkout_Date = models.DateField(auto_now=False, auto_now_add=False)


class Cancellation_Policy(models.Model):
    Description = models.TextField()
    Start_Date = models.DateField(auto_now=False, auto_now_add=False)
    End_Date = models.DateField(auto_now=False, auto_now_add=False)


class Booking(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Cancellation_Policy = models.ForeignKey(Cancellation_Policy, on_delete=models.CASCADE)
    MoneyToPay = models.DecimalField(max_digits=20, decimal_places=2)
    MoneyToRefund = models.DecimalField(max_digits=20, decimal_places=2)
    DateOfBooking = models.DateField(auto_now=False, auto_now_add=False)
    DateOfCancellation = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.User


class Flight_Booking(models.Model):
    Booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE)


class Hotel_Booking(models.Model):
    Booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    Hotel_Room = models.ForeignKey(Hotel_Room, on_delete=models.CASCADE)


class Admin(models.Model):
    Name = models.CharField(max_length=200)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Payment_Log(models.Model):
    Admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Booking = models.ForeignKey(Booking, on_delete=models.CASCADE)


class Cancellation_Log(models.Model):
    Admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Booking = models.ForeignKey(Booking, on_delete=models.CASCADE)