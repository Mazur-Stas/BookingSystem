from django.urls import path
from .views import (
    RoomListView,
    RoomDetailView,
    BookingCreateView,
    BookingUpdateView,
    BookingDeleteView,
    MyBookingsView,
)

app_name = "booking"

urlpatterns = [
    path("", RoomListView.as_view(), name="room_list"),

    path("room/<int:pk>/",RoomDetailView.as_view(),name="room_detail",),

    path("booking/create/",BookingCreateView.as_view(),name="booking_create",),

    path("booking/<int:pk>/edit/",BookingUpdateView.as_view(),name="booking_update",),

    path("booking/<int:pk>/delete/",BookingDeleteView.as_view(),name="booking_delete",),

    path("my-bookings/",MyBookingsView.as_view(),name="my_bookings",),
]