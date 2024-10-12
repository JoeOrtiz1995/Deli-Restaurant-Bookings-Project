from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_agenda(request):
    return HttpResponse("Hello, I'll be the events page!")