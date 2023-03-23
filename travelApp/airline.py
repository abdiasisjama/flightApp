from django import forms
from .models import Airline

INPUT_CLASSES = 'w-1/2 py-2 px-6 rounded-xl border'

class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ["name", "number", "airport"]

        widgets = {
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'number':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'airport':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),

        }
