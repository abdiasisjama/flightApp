from django import forms
from .models import Booking

INPUT_CLASSES = 'w-1/2 py-2 px-6 rounded-xl border'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["ticket_number", "confirmation_number", "price", "issue_date", "passenger", "flight"]

        widgets = {
            'ticket_number':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'confirmation_number':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.NumberInput(attrs={
                'class':INPUT_CLASSES
            }),
            'issue_date':forms.DateTimeInput(attrs={
                'class':INPUT_CLASSES, 'type': 'datetime-local'
            }),
            'passenger':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),

            'flight': forms.Select(attrs={
                'class':INPUT_CLASSES
            })

        }

class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["id" ,"ticket_number", "confirmation_number", "price", "issue_date", "passenger", "flight"]

        widgets = {
            'ticket_number':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),

            'confirmation_number':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.NumberInput(attrs={
                'class':INPUT_CLASSES
            }),
            'issue_date':forms.DateTimeInput(attrs={
                'class':INPUT_CLASSES
            }, format='%d/%m/%Y %H:%M'),
            'passenger':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),

            'flight': forms.Select(attrs={
                'class':INPUT_CLASSES
            })

        }
