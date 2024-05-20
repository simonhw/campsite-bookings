from home.models import Booking
from django import forms
from django.forms.widgets import DateInput, SelectDateWidget

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
            'arrival': DateInput(),
            'departure': DateInput(),
        }