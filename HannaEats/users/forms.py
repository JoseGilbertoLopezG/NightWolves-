# Django
from django import forms
from django.forms import ModelForm, Form
from django.core.exceptions import ValidationError

# Auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

# Modelos
from users.models import *
from food.models import Alimento

class DirectionsForm(forms.Form):
    """Define un formulario para registrar una direccion"""
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
        

class ClienteForm(UserCreationForm):
    """Define un formulario para crear Cliente"""
    
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["correo"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['Ya existe una cuenta con este correo'])
    
    class Meta(UserCreationForm):
        model = Account
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']
        labels = {
            'nombre': ('Nombre'),
            'ap_paterno': ('Apellido Paterno'),
            'ap_materno': ('Apellido Materno*'),
            'correo': ('Correo electrónico'),
            'telefono': ('Número de teléfono*')
        }

class RepartidorForm(UserCreationForm):
    """Define un formulario para crear Repartidor"""
    
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["correo"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['Ya existe una cuenta con este correo'])
    
    class Meta(UserCreationForm):
        model = Account
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']
        labels = {
            'nombre': ('Nombre'),
            'ap_paterno': ('Apellido Paterno'),
            'ap_materno': ('Apellido Materno*'),
            'correo': ('Correo electrónico'),
            'telefono': ('Número de teléfono*')
        }

class AccountModifyForm(UserChangeForm):
    """Define un formulario para modificar una cuenta"""
    class Meta:
        model = Account
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']
        labels = {
            'nombre': ('Nombre'),
            'ap_paterno': ('Apellido Paterno'),
            'ap_materno': ('Apellido Materno*'),
            'correo': ('Correo electrónico'),
            'telefono': ('Número de teléfono*')
        }

class AccountLoginForm(Form):
    """Define un formulario para iniciar sesión"""
    username = forms.EmailField(max_length=150,
                                help_text='Escribe un correo adecuado',
                               error_messages=
                               {'invalid':"Necesitas escribir un correo valido",
                                'required':'Es necesario llenar este campo',
                                "max_length":"El correo solo puede tener 150 caracteres máximo"})
    password = forms.CharField()
    #password = forms.PasswordInput()
    labels = {
        'username': ('Correo electrónico'),
        'password': ('Contraseña'),
    }
