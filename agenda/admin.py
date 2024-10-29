from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'start_date')
    search_fields = ['title', 'start_date']
    list_filter = ('title', 'start_date',)
    summernote_fields = ('description',)


# Register your models here.
#admin.site.register(Event)