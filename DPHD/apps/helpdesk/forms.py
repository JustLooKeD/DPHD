from .models import Ticket
from django.forms import ModelForm, TextInput, Textarea


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }