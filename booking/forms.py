from home.models import Booking
from django import forms
from django.forms.widgets import DateInput, SelectDateWidget, NumberInput

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
            'arrival': DateInput(attrs={'type': 'date'}),
            'departure': DateInput(attrs={'type': 'date'}),
        }