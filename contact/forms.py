from .models import BookingRequest
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ('full_name', 'date_request', 'time_request', 'guests', 'email', 'message')