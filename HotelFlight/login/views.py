from django.shortcuts import render

from datetime import date
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from django import forms
#from .forms import RegisterForm
from database.models import Profile
from django.contrib import auth
# Create your views here.







def login(request):
    if request.method == 'POST':
        UserName = request.POST.get("username","")
        Password = request.POST.get("pass","")
        print(UserName)
        print(Password)
        user = auth.authenticate(username=UserName, password=Password)
        if user is not None:
            print("Correct!")
        else:
            print("Invalid password.")


    return render(request, "login.html")
'''def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")'''
