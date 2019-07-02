from django.shortcuts import render
from .forms import ProfileForm, UserCreateForm
from django.http import HttpResponseRedirect
from django.contrib import auth,messages


# Create your views here.


def login(request):
    redirect_to = request.GET.get('next', '')
    print('kkk  '+redirect_to)
    if request.method == 'POST':
        Username = request.POST.get("username", "")
        Password = request.POST.get("pass", "")
        print(Username)
        print(Password)
        user = auth.authenticate(request, username=Username, password=Password)
        if user is not None:
            print("Correct!")
            auth.login(request, user)
            return HttpResponseRedirect(redirect_to)
        else:
            print("Invalid password.")
            messages.error(request, 'Username or password not correct')
    return render(request, "login/login.html")


def reg(request):
    submitted = False
    if request.method == 'POST':
        userform = UserCreateForm(request.POST)
        profileform = ProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            print('Account created successfully')
        else:
            print('ERRRR')
            print(userform.errors)
    else:
        userform = UserCreateForm()
        profileform = ProfileForm()
    return render(request, "login/reg.html", {'userform': userform, 'profileform': profileform, 'submitted': submitted})
