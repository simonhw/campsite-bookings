from django.db import models
from django.contrib.auth.models import User

ACCOMODATION = ((0, 'Tent'), (1, 'Van'), (2, 'Caravan'), (3, 'Yurt'))

# Create your models here.
class Booking(models.Model):
    booking_id = models.PositiveIntegerField(unique=True)
    booked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    accomodation = models.TextField(choices=ACCOMODATION, default=0)
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
    adults = models.IntegerField()
    children = models.IntegerField()