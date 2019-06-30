from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SearchHotelForm


# Create your views here.


def homepage(request):
    if request.method == "POST":
        form = SearchHotelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['hoteldest'])
            print(form.cleaned_data['checkin'])
            print("valid")
        else:
            print(form.errors)
    else:
        form = SearchHotelForm()
    return render(request, "search/homepage.html", {'form': form})


@login_required(login_url='/login/')
def test(request):
    return render(request, "search/homepage.html")
