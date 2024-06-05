from django.shortcuts import render
from .forms import BookingForm
from .models import Booking
from datetime import datetime
from django.views import generic
from django.contrib import messages

# Create your views here.
class UserBookings(generic.ListView):
    '''
    View that shows bookings made by users ordered by arrival date in
    descending order.
    The path for the template used to render the list is declared. 
    '''

    queryset = Booking.objects.all().order_by('-arrival')
    template_name = 'booking/user_bookings.html'

def booking_view(request):
    '''
    Method to handle the booking form.

    Method processes the user-submitted data and checks if it is valid.
    If it is, the method saves the data and assigns the current user as the
    booking's creator.
    A message is shown on the front-end to denote a successful booking.
    If the data is invalid, the form is re-rendered and shows appropriate
    error messages.
    '''

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