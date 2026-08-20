from django import forms

from booking.models import Room
from .models import EmailLog


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "name",
            "description",
            "image",
            "floor",
            "capacity",
            "is_active",
        ]


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailLog
        fields = [
            "recipient",
            "subject",
            "message",
        ]