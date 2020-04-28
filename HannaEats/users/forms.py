"""Artist forms."""
# Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from users.models import Direcciones

from django.db import models


class DirectionsForm(forms.Form):

    calle = forms.CharField(max_length = 60)
    numero_lt = forms.CharField(max_length = 5)
    numero_mz = forms.CharField(max_length = 5)
    numero_interior = forms.CharField(max_length = 5)
    colonia = forms.CharField(max_length = 20)
    delegacion = forms.CharField(max_length = 20)
    cp = forms.CharField(max_length = 10)
    
class DirectionsForm(forms.ModelForm):
    class Meta:
        model = Direcciones
        fields = ('calle', 'numero_lt','numero_mz','numero_interior','colonia','delegacion','cp')
        labels = {
            'calle': ('Calle'),
            'numero_lt': ('Lt'),
            'numero_mz': ('Mz'),
            'numero_interior': ('Num. Interior*'),
            'colonia': ('Colonia'),
            'delegacion': ('Delegación'),
            'cp' : ('Código Postal'),
        }
        
        """help_texts = {
            'name': ('Agrega el nombre del artista'),
        }
        error_messages = {
            'name': {
                'max_length': ("This Artist's name is too long."),
            },
        }"""
