from django import forms
from .models import people
class peopleForm(forms.ModelForm):
    class Meta:
        model = people
