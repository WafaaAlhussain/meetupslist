from dataclasses import field
import imp
from pyexpat import model
from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your Email')
