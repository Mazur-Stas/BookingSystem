from django.contrib import admin
from .models import Room, Booking

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "floor", "capacity", "is_active")
    list_filter = ("floor", "is_active")
    search_fields = ("name",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "room", "booking_date", "start_time", "end_time", "status")
    list_filter = ("status", "booking_date")
    search_fields = ("user__username", "room__name")


