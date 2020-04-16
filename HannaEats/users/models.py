from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def numero_telefono(value):
    """Verifica que un Charfield sólo contenga números """
    for e in value:
        if(e == ' ' or (e >= '0' and e <= '9')):
            raise ValidationError(
                _('%(value)s no es un número de teléfono válido'),
                code='numbersOnly',
                params={'value': value},
                )

class Cliente(models.Model):
    """Modelo para la BD de un cliente"""
    nombre = models.CharField(max_length = 80)
    ap_paterno = models.CharField(max_length = 110)
    ap_materno = models.CharField(blank = True, max_length = 110)
    correo = models.EmailField(max_length = 300)
    telefono = models.CharField(validators=[numero_telefono], max_length=20)
    direccion = models.CharField(max_length=300)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    def __str__(selfie):
        """Obtener represencacion como cadena"""
        return f"{selfie.nombre} {selfie.ap_paterno} {selfie.ap_materno} \n {selfie.direccion}"

    def __repr__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.__str__()

class Direcciones(models.Model):
    
    calle = models.CharField(max_length = 60)
    numero_lt = models.CharField(max_length = 5)
    numero_mz = models.CharField(max_length = 5)
    numero_interior = models.CharField(blank = True, max_length = 5)
    colonia = models.CharField(max_length = 20)
    delegacion = models.CharField(max_length = 20)
    cp = models.CharField(max_length = 10)
    
    def __str__(selfie):
        """Obtener represencacion como cadena"""
        return f"{selfie.calle} #{selfie.numero}, {selfie.colonia} \n {selfie.delegacion}"

    def __repr__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.__str__()


class Repartidor(models.Model):
    """Modelo para la BD de un repartidor"""
    nombre = models.CharField(max_length = 80)
    ap_paterno = models.CharField(max_length = 110)
    ap_materno = models.CharField(blank = True, max_length = 110)
    correo = models.EmailField(max_length = 300)
    telefono = models.CharField(validators=[numero_telefono], max_length=20)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    def __str__(selfie):
        """Obtener represencacion como cadena"""
        return f"{selfie.name} {selfie.ap_paterno} {selfie.ap_materno} \n {selfie.correo}"

    def __repr__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.__str__()
    

class Admin(models.Model):
    """Modelo para la BD de un cliente"""
    nombre = models.CharField(max_length = 80)
    ap_paterno = models.CharField(max_length = 110)
    ap_materno = models.CharField(blank = True, max_length = 110)
    correo = models.EmailField(max_length = 300)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    def __str__(selfie):
        """Obtener represencacion como cadena"""
        return f"{selfie.name} {selfie.ap_paterno} {selfie.ap_materno} \n {selfie.correo}"

    def __repr__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.__str__()


class ClienteForm(ModelForm):
    """Define un formulario para crear Cliente"""
    class Meta:
        model = Cliente
        fields = ['nombre', 'ap_paterno', 'ap_materno']

class RepartidorForm(ModelForm):
    """Define un formulario para crear Repartidor"""
    class Meta:
        model = Repartidor
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']
