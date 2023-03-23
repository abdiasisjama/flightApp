from django import forms
from .models import Airport

INPUT_CLASSES = 'w-1/2 py-2 px-6 rounded-xl border'

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ["departure_name", "arrival_name", "IATA_code"]

        widgets = {
            'departure_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'arrival_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'IATA_code':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

        }
