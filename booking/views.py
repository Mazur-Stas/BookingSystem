from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room, Booking

class RoomListView(ListView):
    model = Room
    template_name = "booking/room_list.html"
    context_object_name = "rooms"

    def get_queryset(self):
        return Room.objects.filter(is_active=True)

class RoomDetailView(DetailView):
    model = Room
    template_name = "booking/room_detail.html"
    context_object_name = "room"

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = [
        "room",
        "booking_date",
        "start_time",
        "end_time",
        "purpose",
    ]

    template_name = "booking/booking_form.html"
    success_url = reverse_lazy("booking:my_bookings")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = [
        "room",
        "booking_date",
        "start_time",
        "end_time",
        "purpose",
        "status",
    ]

    template_name = "booking/booking_form.html"
    success_url = reverse_lazy("booking:my_bookings")

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = "booking/booking_confirm_delete.html"
    success_url = reverse_lazy("booking:my_bookings")

class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "booking/my_bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user
        ).order_by("-booking_date")



