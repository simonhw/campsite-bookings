from django.db import models
from django.contrib.auth.models import User

# ACCOMMODATION = ((0, 'Tent'), (1, 'Van'), (2, 'Caravan'), (3, 'Yurt'))

# Create your models here.
class Booking(models.Model):
    ACCOMMODATION = ((0, 'Tent'), (1, 'Van'), (2, 'Caravan'), (3, 'Yurt'))

    booking_id = models.CharField(max_length=15, unique=True)
    booked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    accommodation = models.IntegerField(choices=ACCOMMODATION, default=0)
    arrival = models.DateField()
    departure = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    booked = models.BooleanField(default=False)

    class Meta:
        ordering = ["arrival"]
    
    def __str__(self):
        return f'{self.arrival} | \
            {dict(self.ACCOMMODATION).get(self.accommodation)} booking | \
                {self.booked_by.first_name} {self.booked_by.last_name} | \
                    Booking id: {self.booking_id}'