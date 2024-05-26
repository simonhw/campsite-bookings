from django.shortcuts import render
from .forms import BookingForm
from home.models import Booking
from datetime import datetime
from django.views import generic
from django.contrib import messages

# Create your views here.
class UserBookings(generic.ListView):
    queryset = Booking.objects.all().order_by('-arrival')
    template_name = 'booking/user_bookings.html'

def booking_view(request):
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booked_by = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS, "Booking received! Confirmation "
                "will follow after payment is completed."
                )
        else:
            booking_form = BookingForm(data=request.POST)
            return render(
                request,
                "booking/booking.html",
                {
                    "booking_form": booking_form,
                },
            )

    booking_form = BookingForm()

    return render(
        request,
        "booking/booking.html",
        {
            "booking_form": booking_form,
        },
    )