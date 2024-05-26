from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.
class BookingList(generic.ListView):
    queryset = Booking.objects.all().order_by('arrival')
    template_name = 'home/index.html'