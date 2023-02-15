from django import forms
from .models import *


class regform(forms.ModelForm):
    class Meta:
        model=regmodel
        fields='__all__'


class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class fileForm(forms.ModelForm):
    class Meta:
        model=fileModel
        fields='__all__'

