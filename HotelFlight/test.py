from database.models import Hotel, Hotel_Room, Room
from django.db.models import Q, Count
from datetime import date
from django.db import connection
from django.core.paginator import Paginator
from collections import namedtuple


def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


dest = ''
ddd = date(2019, 6, 22)

ar = Hotel_Room.objects.select_related('Hotel').filter((Q(Hotel__Hotel_Name__icontains=dest) |
                                                        Q(Hotel__Hotel_Location__icontains=dest)) &
                                                       (Q(Checkout_Date__lte=ddd)
                                                        ))

cursor = connection.cursor()

dest = '%Bangladesh%'
checkin = '2019-09-09'
ddd = date(2019, 9, 22)
cnt=1
cursor.execute("SELECT H.Hotel_Name,H.Hotel_Location,H.Hotel_Country,H.Description,count(*) as 'Num',"
               "min(HR.Price) as 'Price' FROM database_hotel_room HR join database_hotel H on(HR.Hotel_id=H.id)"
               "where ((lower(H.Hotel_Name) Like %s OR lower(H.Hotel_Location) Like %s OR "
               "lower(H.Hotel_Country) Like %s) and HR.Checkout_Date <= %s)"
               "GROUP BY H.Hotel_Name HAVING Num >= %s", [dest, dest, dest, checkin,cnt])
data = namedtuplefetchall(cursor)

p = Paginator(data, 7)

r1 = p.page(1)

# print(r1.object_list)

for rrr in r1.object_list:
    print(rrr.Hotel_Name + '  ' + rrr.Hotel_Location + '   ' + str(rrr.Num) + '   ' + str(rrr.Price))
    print(' ')
