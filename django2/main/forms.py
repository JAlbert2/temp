from django import forms
from datetime import datetime
from django.forms import ModelForm
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("user", 'age', 'creation', 'covid')
        
class xapiForm(forms.Form):
    g = forms.BooleanField(label = 'Gorilla', required=False)
    d = forms.BooleanField(label = 'Dolphin', required=False)
    f = forms.BooleanField(label = 'Fox', required=False)
    
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)