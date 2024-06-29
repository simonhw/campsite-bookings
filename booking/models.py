from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, timedelta
import uuid


class Booking(models.Model):
    """
    A model for campsite bookings.

    Fields:
        ACCOMMODATION (Tuple) - A set of options for accomodation type.
        booking_id (CharField) - A universally unique identifier for the
                                 booking.
        booked_by (ForeignKey) - The user who created the booking referenced
                                 from the Django User model.
        created_on (DateTimeField) - The date and time the booking was created.
        updated_on (DateTimeField) - The date and time the booking was last
                                     updated.
        accommodation (IntegerField) - The integer choice corresponding to the
                                       string in the ACCOMODATION tuple.
        arrival (DateField) - The arrival date for the booking.
        departure (DateField) - The departure date for the booking.
        adults (PositiveIntegerField) - An integer number of adults in the
                                        booking with a minimum value of 1.
        children (PositiveIntegerField) - An integer number of children in the
                                          booking with a minimum value of 0.
        booked (BooleanField) - The booking status of the booking request:
                                either booked or pending.
    """

    ACCOMMODATION = ((0, 'Tent'), (1, 'Van'), (2, 'Caravan'), (3, 'Yurt'))

    booking_id = models.CharField(max_length=36, default=uuid.uuid4)
    booked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    accommodation = models.IntegerField(choices=ACCOMMODATION, default=0)
    arrival = models.DateField()
    departure = models.DateField()
    adults = models.PositiveIntegerField(default=1,
                                         validators=[MinValueValidator(1), MaxValueValidator(10)])
    children = models.PositiveIntegerField(default=0,
                                         validators=[MaxValueValidator(10)])
    booked = models.BooleanField(default=False)

    class Meta:
        """
        Meta class for the booking form. Specifies how to sort the bookings
        in querysets.
        """

        ordering = ["arrival"]

    def __str__(self):
        """
        Method to return a string with relevant booking details.

        Returns the arrival date, accomodation type, name of the user who made
        the booking, the the unique booking ID.
        """

        return f'{self.arrival} | \
            {dict(self.ACCOMMODATION).get(self.accommodation)} booking by \
                {self.booked_by.first_name} {self.booked_by.last_name} | \
                    Booking id: {self.booking_id}'

    def string_from_tuple(self):
        """
        Method to return the string value of the accomodation type from the
        ACCOMODATION tuple.
        """

        return f'{dict(self.ACCOMMODATION).get(self.accommodation)}'

    def is_in_past(self):
        """
        Method to return a boolean True if the departure date is in the past,
        and False if it is not.
        """

        return date.today() > self.departure

    def is_within_48h(self):
        """
        Method to return a boolean True is the arrival date is within the next
        48 hours, and false if it is not.
        """

        return self.arrival < date.today() + timedelta(hours=48)

    def full_name(self):
        """
        Method to return the full name of the user who made a given booking
        in the form of a string.
        """
        if self.booked_by.first_name:
            return f'{self.booked_by.first_name} {self.booked_by.last_name}'
        else:
            return False
