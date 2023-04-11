from django import forms
from .models import Login
# ........................

class MyLoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'password']