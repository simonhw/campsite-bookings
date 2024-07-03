from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Class to sort the bookings more effectively when being viewed in
    the admin panel.
    """

    list_display = ('booked_by', 'arrival', 'accommodation')
    search_fields = ['arrival']
    list_filter = ('accommodation',)
