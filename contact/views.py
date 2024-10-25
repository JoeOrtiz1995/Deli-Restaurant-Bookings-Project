from django.shortcuts import render
from .models import About
from .forms import BookingForm

# Create your views here.
def about_us(request):
    """
    Renders the About us and Bookings section.
    """
    contact = About.objects.all().last()
    booking_form = BookingForm()

    return render(
        request, 
        "contact/contact.html",
        {"contact": contact,
         "booking_form": booking_form
         },
    )
