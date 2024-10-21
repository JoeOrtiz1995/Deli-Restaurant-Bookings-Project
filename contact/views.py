from django.shortcuts import render
from .models import About

# Create your views here.
def about_us(request):
    """
    Renders the About us and Bookings section.
    """
    contact = About.objects.all().last()

    return render(
        request, 
        "contact/contact.html",
        {"contact": contact},
    )
