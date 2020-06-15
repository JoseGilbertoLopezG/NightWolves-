# Django
from django.utils import timezone
from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import NON_FIELD_ERRORS
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Auth
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import AccountManager

def numero_telefono(value):
    """Verifica que un charfield tenga una longitud adecuada y que sólo contenga números"""
    if len(value) < 8:
        raise ValidationError(
            _('%(value)s Es demasiado corto'),
            code='min_length',
            params={'value': value},
            )
    for e in value:
        if(e >= '0' and e <= '9'):
            return
        else:
            raise ValidationError(
                _('%(value)s Sólo debe contener números'),
                code='invalid',
                params={'value': value},
                )
        
def numeros(value):
    """Verifica que un charfield solo contenga numeros"""
    for e in value:
        if(e >= '0' and e <= '9'):
            return
        else:
            raise ValidationError(
                _('%(value)s Sólo debe contener números'),
                code='invalid',
                params={'value': value},
                )
        
class Account(AbstractBaseUser, PermissionsMixin):
    """Modelo para la BD de una cuenta"""
    nombre = models.CharField(max_length = 80,
                              error_messages=
                              {"required":"Necesitas escribir un nombre",
                               "max_length":"Tu nombre debe teer 80 caracteres máximo"})
    ap_paterno = models.CharField(max_length = 110,
                                  error_messages=
                                  {"required":"Necesitas escribir un appelido",
                                   "max_length":"Tu apellido debe teer 110 caracteres máximo"})
    ap_materno = models.CharField(blank=True, max_length = 110,
                                  error_messages={"max_length":"Tu apellido debe teer 110 caracteres máximo"})
    correo = models.EmailField(unique=True, max_length = 150,
                               error_messages=
                               {'invalid':"Necesitas escribir un email valido",
                                'unique':"Este email ya esta en uso",
                                'required':'Es necesario dar un email',
                                "max_length":"Tu email solo puede tener 150 caracteres máximo"})
    telefono = models.CharField(blank=True, max_length = 20,
                                validators=[numero_telefono],
                                help_text='Escribe numeros sin espacio Ej 5522009117',
                                error_messages=
                                {'required':'Es necesario dar un email',
                                 "max_length":"Tu email solo puede tener 20 caracteres máximo"})
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    # Perrmisos y auth
    TIPOS_DE_USUARIO = ( 
        (1, "Admin"), 
        (2, "Repartidor"), 
        (3, "Cliente")
    )
    tipo = models.PositiveSmallIntegerField(choices=TIPOS_DE_USUARIO)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'ap_paterno']
    objects = AccountManager()    
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        ''' dirs_str = ""
        dirs = list(Direcciones.direccion.all())
        if len(dirs) == 0:
            return f"{self.nombre} {self.ap_paterno} {self.ap_materno}"
            
        dirs_str += f"{dirs[0].__str__()}"
        for dir in dirs[1:]:
            dirs_str += f"{dir.__str__()}"
        return f"Dirección: {dirs_str}"  '''
        
        return f"{self.nombre} {self.ap_paterno} {self.ap_materno}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
    

class Direcciones(models.Model):
    "Clase para representar direcciones"
    calle = models.CharField(max_length = 60,null=False, error_messages={'required':'Es necesario dar una calle', "max_length":"La calle puede tener 60 caracteres maximo"})
    
    numero_lt = models.CharField(max_length = 5, null=False, validators=[numeros], error_messages={'required':'Este campo es obligatorio', "max_length":"La longitud máxima es de 5 caracteres"})
    numero_mz = models.CharField(max_length = 5, null=False, validators=[numeros], error_messages={'required':'Este campo es obligatorio', "max_length":"La longitud máxima es de 5 caracteres"})    
    numero_interior = models.CharField(blank = True, max_length = 5, validators=[numeros], error_messages={"max_length":"La longitud máxima es e 5 caracteres"})
    
    cp = models.CharField(max_length = 10, null=False, validators=[numeros], error_messages={'required':'Es necesario dar un codigo postal', "max_length":"El codigo postal puede tener 10 caracteres maximo"})
    
    colonia = models.CharField(max_length = 40,null=False)
    delegacion = models.CharField(max_length = 20,null=False)
    
    # Relaciones de entidad
    direccion = models.ManyToManyField("users.Account", related_name="usuario_asociado")
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        #dirs = list(self.all())
        if f"{self.numero_interior}" == "" and f"{self.numero_interior}" == " " and f"{self.calle}" == "" and f"{self.calle}" == " ":
            return f"No tienes ninguna Direccion"
        elif f"{self.numero_interior}" == "" or f"{self.numero_interior}" == " ":
            return f"{self.calle} Mz. {self.numero_mz}, Lt. {self.numero_lt}, {self.colonia}, {self.delegacion}, Cp. {self.cp}"
        else:
            return f"{self.calle} Mz. {self.numero_mz}, Lt. {self.numero_lt}, No. Int. {self.numero_interior}, {self.colonia}, {self.delegacion}, Cp. {self.cp}"
    
    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
