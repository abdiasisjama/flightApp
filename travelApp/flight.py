from django import forms
from .models import Flight

INPUT_CLASSES = 'w-1/2 py-2 px-6 rounded-xl border'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ["flight_number", "checking_time", "departure_time", "arrival_time", "duration_in_min", "flight_class", "airport"]

        widgets = {
            'flight_number':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'checking_time':forms.DateTimeInput(attrs={
                'class':INPUT_CLASSES, 'type': 'datetime-local'
            },),
            'departure_time':forms.DateTimeInput(attrs={
                'class':INPUT_CLASSES, 'type': 'datetime-local'
            }),
            'arrival_time':forms.DateTimeInput(attrs={
                'class':INPUT_CLASSES, 'type': 'datetime-local'
            }),
            'duration_in_min':forms.NumberInput(attrs={
                'class':INPUT_CLASSES,
            }),

            'flight_class': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),

            'airport': forms.Select(attrs={
                'class':INPUT_CLASSES
            })

        }

