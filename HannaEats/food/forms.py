# Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from users.models import Direcciones
from food.models import Alimento
from food.models import Categoria
from food.models import OrdenComida
from food.models import CantidadAlimento

from django.db import models

class FoodForm(forms.Form):
    
    nombre = forms.CharField(max_length=120)
    descripcion = forms.CharField(max_length=200)
    precio = forms.CharField(max_length=200)
    foto = forms.ImageField()
    
    def clean_food(self):
        data = self.cleaned_data["nombre"]
        if Alimento.objects.filter(nombre=data).count() > 0:
            raise forms.ValidationError("Un akimento con este nombre ya existe")

        return data

class FoodForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ('nombre','descripcion','precio','foto','categoria')
        labels = {
            'nombre': ('Nombre'),
            'descripcion': ('Descripcion'),
            'precio' : ('Precio'),
            'foto' : ('Imágen'),
            'categoria':('Categoría'),
        }
        error_messages = {
            'nombre': {
                'unique': ("Alimento ya existente en la base de datos"),
            },
            'descripcion': {
                'unique': ("Alimento con esa descripcion ya existe en la base de datos"),
            },
        }
        
    def clean_food(self):
        data = self.cleaned_data["nombre"]
        if Alimento.objects.filter(nombre=data).count() > 0:
            raise forms.ValidationError("Un akimento con este nombre ya existe")

        return data
    
class CategoryForm(forms.Form):
    
    nombre = forms.CharField(max_length=120)
    imagen = forms.ImageField()
    
    def clean_food(self):
        data = self.cleaned_data["nombre"]
        if Alimento.objects.filter(nombre=data).count() > 0:
            raise forms.ValidationError("Una categoria con este nombre ya existe")

        return data

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','imagen']
        labels = {
            'nombre': ('Nombre'),
            'imagen' : ('Imágen'),
        }
        error_messages = {
            'nombre': {
                'unique': ("Categoria existente en la base de datos"),
            },
        }
        
    def clean_food(self):
        data = self.cleaned_data["nombre"]
        if Alimento.objects.filter(nombre=data).count() > 0:
            raise forms.ValidationError("Una categoria con este nombre ya existe")

        return data

            
class CantidadAlimentoForm(forms.ModelForm):
    
    cantidad = models.IntegerField()
    
    class Meta:
        model = CantidadAlimento
        fields = ['cantidad']
        labels = {
            'cantidad': ('Cantidad'),
        }
