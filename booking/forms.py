from .models import Booking
from django import forms
from django.forms.widgets import DateInput, SelectDateWidget, NumberInput
from datetime import date, timedelta
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    """
    Form for making campsite bookings. The user can specify the type of
    booking, the arrival and departure dates, and the number of adults and
    children in the booking.
    """

    class Meta:
        """
        Meta class for the form's metadata. Specifies the model to be used
        with the form and the fields to use. Widget attributes are also 
        specified in this class.
        """

        model = Booking
        fields = (
            'accommodation',
            'arrival',
            'departure',
            'adults',
            'children',
        )
        widgets = {
            'arrival': DateInput(attrs={
                'type': 'date',
                'id': 'arrival',
                'min': date.today() + timedelta(days=1)
                }),
            'departure': DateInput(attrs={
                'type': 'date',
                'id': 'departure',
                'min': date.today() + timedelta(days=2)
                }),
        }

    def clean(self):
        """
        Validation of form data on the back-end.

        The method ensures that the departure date can neither be on the same
        date as the arrival nor can it be before the date of arrival.

        If the data validates, the method returns the cleaned data.
        If invalid, it raises a validation error to inform the user.
        """
        
        cleaned_data = super().clean()
        arrival = cleaned_data.get('arrival')
        departure = cleaned_data.get('departure')

        if arrival > departure:
            raise ValidationError('Please select a departure date after your'
                                  ' arrival.')

        if arrival == departure:
            raise ValidationError('The minimum length of stay is one night.')
        
        return cleaned_data