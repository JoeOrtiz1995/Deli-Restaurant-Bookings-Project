from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import BookingForm

# Create your views here.
def about_us(request):
    """
    Renders the About us and Bookings section.
    """
    if request.method =="POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(request, messages.SUCCESS, 
                                 "Booking request received!")

    about = About.objects.all().last()
    booking_form = BookingForm()

    return render(
        request, 
        "contact/contact.html",
        {"about": about,
         "booking_form": booking_form,
         },
    )
