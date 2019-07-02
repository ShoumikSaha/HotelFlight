from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SearchHotelForm
from django.db import connection


# Create your views here.


def homepage(request):
    if request.method == "POST":
        form = SearchHotelForm(request.POST)
        if form.is_valid():
            dest = form.cleaned_data['hoteldest']
            checkindate = form.cleaned_data['checkin']
            checkoutdate = form.cleaned_data['checkout']
            room_count = form.cleaned_data['room']
            adult_count = form.cleaned_data['adult']
            print(form.cleaned_data['hoteldest'])
            print(form.cleaned_data['checkin'])
            print(form.cleaned_data['checkout'])
            print(form.cleaned_data['room'])
            print(form.cleaned_data['adult'])
            print(form.cleaned_data['children'])
            #            print("valid")
            cursor = connection.cursor()
            cursor.execute('''SELECT H.Hotel_Name,R.RoomType,HR.Price FROM database_hotel H JOIN database_hotel_room HR ON (H.id = HR.Hotel_id)
            JOIN database_room R ON (R.id = HR.Room_id) WHERE H.Hotel_Location=%s AND HR.Checkout_Date <= %s''',
                           [dest, checkindate])
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            print(form.errors)
    else:
        form = SearchHotelForm()
    return render(request, "search/homepage.html", {'form': form})


def searchHotelPage(request):
    dest = request.GET.get('hoteldest', '')
    checkindate = request.GET.get('checkin', '')
    checkoutdate = request.GET.get('checkout', '')
    room_count = request.GET.get('room', '')
    adult_count = request.GET.get('adult', '')
    print(dest)
    print(checkindate)
    print(checkoutdate)
    print(room_count)
    print(adult_count)
    cursor = connection.cursor()
    cursor.execute('''SELECT H.Hotel_Name,H.Hotel_Location,H.Hotel_Country,H.Description,R.RoomType,HR.Price,R.AirConditioner,HR.Complimentary_Breakfast,HR.Wifi FROM database_hotel H JOIN database_hotel_room HR ON (H.id = HR.Hotel_id)
                JOIN database_room R ON (R.id = HR.Room_id) WHERE H.Hotel_Location=%s AND HR.Checkout_Date <= %s''',
                   [dest, checkindate])
    data = cursor.fetchall()
    for row in data:
        print(row)
        print(type(row[8]))
    return render(request, "search/searchHotel.html", {'data': data})


@login_required(login_url='/login/')
def test(request):
    return render(request, "search/test.html")
