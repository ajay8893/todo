from django import forms
from .models import todo


class Todoform(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title', 'description', 'complete']
