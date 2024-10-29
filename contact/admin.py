from django.contrib import admin
from .models import About, BookingRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('title', 'content')

@admin.register(BookingRequest)
class BookingRequestAdmin(SummernoteModelAdmin):
    list_display = ('date_request', 'time_request', 'guests')
    search_fields = ('full_name', 'date_request', 'email')
    list_filter = ('date_request', 'time_request', 'guests', 'full_name',)