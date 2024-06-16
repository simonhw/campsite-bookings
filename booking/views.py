from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import BookingForm
from .models import Booking
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class SuperUserCheck(UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return self.request.user.is_superuser


class UserBookings(LoginRequiredMixin, generic.ListView):
    """
    View that shows bookings made by users ordered by arrival date in
    descending order.
    The path for the template used to render the list is declared.
    """

    template_name = 'booking/user_bookings.html'

    
    def get_queryset(self):
        """
        Method to get a queryset of bookings.

        The queryset is filtered so that only bookings made by the currently
        logged in user can be seen. The bookings are ordered by arrival date
        in descending order.
        """

        queryset = Booking.objects.all().order_by(
            '-arrival'
            ).filter(
                booked_by=self.request.user
                )
        return queryset


class AllBookings(SuperUserCheck, generic.ListView):
    """
    View that shows all bookings ordered by arrival date in descending order.
    The path for the template used to render the list is declared.
    """

    template_name = 'booking/manage_bookings.html'

    
    def get_queryset(self):
        """
        Method to get a queryset of bookings.

        The queryset is filtered so that all bookings are listed ordered by
        arrival date in descending order.
        """

        queryset = Booking.objects.all().order_by('-arrival')
        return queryset


def booking_view(request):
    """
    Method to handle the booking form.

    Method processes the user-submitted data and checks if it is valid.
    If it is, the method saves the data and assigns the current user as the
    booking's creator.
    A message is shown on the front-end to denote a successful booking.
    If the data is invalid, the form is re-rendered and shows appropriate
    error messages.
    """

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


@login_required
def booking_edit(request, id):
    """
    Method to allow user edit a booking.

    Method takes in the booking id and fills the form with the relevant data
    for the user to edit.

    TO-DO: Method verifies that requested booking is being viewed by the user that
    created it. 
    """

    booking = get_object_or_404(Booking, id=id)

    if not booking.booked_by == request.user:
        raise PermissionDenied
    else:
        if booking.booked_by == request.user and request.method == 'GET':
            booking_form = BookingForm(instance=booking)
            return render(request, 'booking/booking.html', {'booking_form': booking_form, 'id': id})
        elif request.method == 'POST':
            booking_form = BookingForm(request.POST, instance=booking)
            if booking_form.is_valid():
                booking_form.save()
                return redirect('user_bookings')
            else:
                return HttpResponseBadRequest('Invalid form data. Please check your inputs.')
        else:
            return HttpResponseBadRequest('Unsupported request method.')


@login_required
def booking_delete(request, id):
    """
    Method to allow a user to delete their booking.

    Method takes in the booking ID and 
    """

    booking = get_object_or_404(Booking, id=id)

    if not booking.booked_by == request.user:
        raise PermissionDenied
    else:
        if booking.booked_by == request.user and not booking.is_within_48h():
            booking.delete()
            messages.add_message(
                    request, messages.SUCCESS, "Booking successfully deleted!"
                    )
        else:
            messages.add_message(
                request, messages.ERROR, "It was not possible to delete this"
                " booking."
            )
        return redirect('user_bookings')
    
