from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BookingForm
from datetime import datetime
from django.contrib import messages

# Create your views here.

def booking_view(request):
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booked_by = request.user
            booking.save()
            # The below code is having no effect...
            messages.add_message(
                request, messages.SUCCESS, "Booking received! Confirmation "
                "will follow after payment is completed."
                )

    booking_form = BookingForm()

    return render(
        request,
        "booking/booking.html",
        {
            "booking_form": booking_form,
        },
    )