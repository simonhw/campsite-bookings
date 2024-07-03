from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import BookingForm
from .models import Booking
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class StaffCheck(UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return self.request.user.is_staff


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


class AllBookings(StaffCheck, generic.ListView):
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
                request, messages.SUCCESS, "Booking received! We will be in "
                "touch to facilitate payment and confirm your booking shortly."
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
    """

    booking = get_object_or_404(Booking, id=id)

    if booking.booked_by == request.user or request.user.is_staff:
        if request.method == 'GET':
            booking_form = BookingForm(instance=booking)
            return render(request, 'booking/booking.html',
                          {'booking_form': booking_form, 'id': id})
        elif request.method == 'POST':
            booking_form = BookingForm(request.POST, instance=booking)
            if booking_form.is_valid():
                booking_form.save()
                messages.add_message(
                    request, messages.SUCCESS, "Booking successfully updated!"
                )
                if request.user.is_staff:
                    return redirect('manage_bookings')
                else:
                    return redirect('user_bookings')
            else:
                booking_form = BookingForm(data=request.POST)
                return render(
                    request,
                    "booking/booking.html",
                    {
                        "booking_form": booking_form,
                    },
                )
                messages.add_message(
                    request, messages.SUCCESS, "Invalid form data."
                                               " Please check your inputs."
                )
        else:
            return HttpResponseBadRequest('Unsupported request method.')
    else:
        raise PermissionDenied


@login_required
def booking_delete(request, id):
    """
    Method to allow a user to delete their booking.

    Method takes in the booking ID and verifies the user's authorisation to
    delete the booking and if the booking is able to be deleted.
    """

    booking = get_object_or_404(Booking, id=id)

    if booking.booked_by == request.user or request.user.is_staff:
        if (booking.booked_by == request.user and
                not booking.is_within_48h()) or request.user.is_staff:
            booking.delete()
            messages.add_message(
                    request, messages.SUCCESS, "Booking successfully deleted!"
                    )
        else:
            messages.add_message(
                request, messages.ERROR, "It was not possible to delete this"
                " booking."
            )
        if request.user.is_staff:
            return redirect('manage_bookings')
        else:
            return redirect('user_bookings')
    else:
        raise PermissionDenied
