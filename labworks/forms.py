from django import forms
from .models import Lab


class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ('name', 'comment', 'file')

