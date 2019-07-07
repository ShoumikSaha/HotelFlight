from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SearchHotelForm
from django.db import connection
from django.core.paginator import Paginator
from collections import namedtuple


# Create your views here.


def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def homepage(request):
    form = SearchHotelForm()
    return render(request, "search/homepage.html", {'form': form})


def searchHotelPage(request):
    form = SearchHotelForm()
    dest = request.GET.get('hoteldest', '')
    checkin = request.GET.get('checkin', '')
    checkout = request.GET.get('checkout', '')
    roomcount = request.GET.get('room', '')
    adultcount = request.GET.get('adult', '')
    print(checkin)
    dest = '%' + dest + '%'
    roomcount = int(roomcount)
    cursor = connection.cursor()
    cursor.execute("SELECT H.Hotel_Name,H.Hotel_Location,H.Hotel_Country,H.Description,count(*) as 'Num',"
                   "min(HR.Price)*%s as 'Price', H.CompanyAdmin_id as ID  FROM database_hotel_room HR "
                   "join database_hotel H on(HR.Hotel_id=H.id)"
                   "where ((lower(H.Hotel_Name) Like %s OR lower(H.Hotel_Location) Like %s OR "
                   "lower(H.Hotel_Country) Like %s) and HR.Checkout_Date <= %s)"
                   "GROUP BY H.Hotel_Name HAVING Num >= %s", [roomcount, dest, dest, dest, checkin, roomcount])
    data = namedtuplefetchall(cursor)
    paginator = Paginator(data, 5)
    page = request.GET.get('page')
    hotels = paginator.get_page(page)
    return render(request, "search/searchHotel.html", {'form': form, 'hotels': hotels})


# @login_required(login_url='/login/')
def test(request):
    return render(request, "search/test.html")
