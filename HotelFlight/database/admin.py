from django.contrib import admin
from .models import Profile, Room, Hotel, Hotel_Room

# Register your models here.
admin.site.register(Profile)
admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Hotel_Room)
