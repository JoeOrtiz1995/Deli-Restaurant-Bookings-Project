from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "agenda/index.html"
    paginate_by = 4