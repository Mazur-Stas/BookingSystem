from django import forms
from .models import Booking, Room


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "room",
            "booking_date",
            "start_time",
            "end_time",
            "purpose",
        ]

        widgets = {
            "booking_date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError(
                "Час завершення має бути пізніше часу початку."
            )

        return cleaned_data


class RoomSearchForm(forms.Form):
    floor = forms.IntegerField(
        required=False,
        min_value=1,
        label="Поверх"
    )

    capacity = forms.IntegerField(
        required=False,
        min_value=1,
        label="Місткість"
    )

    booking_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Дата"
    )