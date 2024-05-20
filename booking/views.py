from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BookingForm
from datetime import datetime

# Create your views here.

# class BookingView(TemplateView):
#     template_name = 'booking/booking.html'

def booking_view(request):
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booked_by = request.user
            booking.save()

    booking_form = BookingForm()

    return render(
        request,
        "booking/booking.html",
        {
            "booking_form": booking_form,
        },
    )