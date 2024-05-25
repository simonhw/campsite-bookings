from home.models import Booking
from django import forms
from django.forms.widgets import DateInput, SelectDateWidget, NumberInput
from datetime import date
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
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
                'min': date.today(),
                }),
            'departure': DateInput(attrs={
                'type': 'date',
                'min': date.today()
                }),
        }

    def clean(self):
        cleaned_data = super().clean()
        arrival = cleaned_data.get('arrival')
        departure = cleaned_data.get('departure')

        if arrival > departure:
            raise ValidationError('Please select a departure date after your arrival.')

        if arrival == departure:
            raise ValidationError('The minimum length of stay is one night.')
        
        return cleaned_data