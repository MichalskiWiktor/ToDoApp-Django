from django import forms
from django.forms import ModelForm
from .models import ListItem


class DateInput(forms.DateInput):
    input_type = 'date'



class NewItemForm(ModelForm):
    # We can create here new fields for our form or use ones already created in models
    class Meta:
        model = ListItem
        fields = ['text', 'deadline', 'status']
        widgets = {
            'deadline': DateInput(),
        }