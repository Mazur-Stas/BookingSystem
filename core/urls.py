from django.urls import path

from .views import (
    HomeView,
    DashboardView,
    BookingRequestsView,
    BookingApproveView,
    BookingRejectView,
    RoomCreateView,
    RoomUpdateView,
    RoomDeleteView,
    StatisticsView,
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("bookings/", BookingRequestsView.as_view(), name="booking_requests"),
    path("bookings/<int:pk>/approve/", BookingApproveView.as_view(), name="booking_approve"),
    path("bookings/<int:pk>/reject/", BookingRejectView.as_view(), name="booking_reject"),
    path("rooms/create/", RoomCreateView.as_view(), name="room_create"),
    path("rooms/<int:pk>/edit/", RoomUpdateView.as_view(), name="room_update"),
    path("rooms/<int:pk>/delete/", RoomDeleteView.as_view(), name="room_delete"),
    path("statistics/", StatisticsView.as_view(), name="statistics"),
]