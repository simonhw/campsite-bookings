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
                'min': date.today()
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

        print(f"Arrival Date: {arrival}")  # Debug statement
        print(f"Departure Date: {departure}")  # Debug statement
        print(arrival <= date.today()) # Debug statement

        if arrival > departure:
            print('Your departure date is invalid!')
            raise ValidationError('Please select a departure date after your arrival.')

        if arrival == departure:
            print('The minimum stay is one night!')
            raise ValidationError('The minimum stay is one night!')
        
        return cleaned_data

    # def clean_arrival(self, value):
    #     if value <= date.now():
    #         raise form.ValidationError('The date cannot be in the past!')
    #     return value
    
    # def clean_departure(self, arrival, value):
    #     if value == arrival:
    #         raise form.ValidationError('Minimun stay is one night!')
    #     return value