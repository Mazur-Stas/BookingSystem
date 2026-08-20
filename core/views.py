from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from booking.models import Room, Booking
from .models import Notification
from .forms import RoomForm

class HomeView(TemplateView):
    template_name = "home.html"

class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, "profile")
            and self.request.user.profile.role == "MANAGER"
        )


class DashboardView(LoginRequiredMixin,ManagerRequiredMixin,TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_rooms"] = Room.objects.count()
        context["total_bookings"] = Booking.objects.count()
        context["new_bookings"] = Booking.objects.filter(
            status="NEW"
        ).count()

        return context


class BookingRequestsView(LoginRequiredMixin,ManagerRequiredMixin,ListView):
    model = Booking
    template_name = "core/booking_requests.html"
    context_object_name = "bookings"
    ordering = ["-created_at"]


class BookingApproveView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.profile.role == "MANAGER"

    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)

        booking.status = "APPROVED"
        booking.save()

        return redirect("core:booking_requests")


class BookingRejectView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.profile.role == "MANAGER"

    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)

        booking.status = "REJECTED"
        booking.save()

        return redirect("core:booking_requests")


class RoomCreateView(LoginRequiredMixin,ManagerRequiredMixin,CreateView):
    model = Room
    form_class = RoomForm
    template_name = "core/room_form.html"
    success_url = reverse_lazy("core:dashboard")


class RoomUpdateView(LoginRequiredMixin,ManagerRequiredMixin,UpdateView):
    model = Room
    form_class = RoomForm
    template_name = "core/room_form.html"
    success_url = reverse_lazy("core:dashboard")


class RoomDeleteView(LoginRequiredMixin,ManagerRequiredMixin,DeleteView):
    model = Room
    template_name = "core/room_confirm_delete.html"
    success_url = reverse_lazy("core:dashboard")


class StatisticsView(LoginRequiredMixin,ManagerRequiredMixin,TemplateView):
    template_name = "core/statistics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_bookings"] = Booking.objects.count()

        context["approved_bookings"] = Booking.objects.filter(
            status="APPROVED"
        ).count()

        context["rejected_bookings"] = Booking.objects.filter(
            status="REJECTED"
        ).count()

        context["new_bookings"] = Booking.objects.filter(
            status="NEW"
        ).count()

        return context