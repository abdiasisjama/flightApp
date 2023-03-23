from django import forms
from .models import Passenger

INPUT_CLASSES = 'w-1/2 py-2 px-6 rounded-xl border'

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["first_name", "middle_name", "last_name", "passport_number", "nationality", "phone", "email"]

        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'middle_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'last_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'passport_number':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'nationality':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'phone': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            })

        }

class EditPassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["first_name", "middle_name", "last_name", "passport_number", "nationality", "phone", "email"]

        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'middle_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'last_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'passport_number':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'nationality':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'phone': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            })

        }
