from django import forms
from .models import Calculation

class calculationForm(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = ['principle', 'rate', 'time']