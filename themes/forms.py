# themes/forms.py

from django import forms
from .models import Theme

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['title', 'description']
