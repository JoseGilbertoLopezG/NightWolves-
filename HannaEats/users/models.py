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

def unique_email_cliente(value):
    clientes = Cliente.objects.all()
    for e in clientes:
        if(e.correo == value):
            raise ValidationError(
                _('%(value)s ya esta en uso por alguien'),
                code='preexisting email',
                params={'value': value},
                )

def unique_email_repartidor(value):
    repartidores = Repartidor.objects.all()
    for e in repartidores:
        if(e.correo == value):
            raise ValidationError(
                _('%(value)s ya esta en uso por alguien'),
                code='preexisting email',
                params={'value': value},
                )

class Cliente(models.Model):
    """Modelo para la BD de un cliente"""
    nombre = models.CharField(max_length = 80)
    ap_paterno = models.CharField(max_length = 110)
    ap_materno = models.CharField(blank = True, max_length = 110)
    correo = models.EmailField(validators=[unique_email_cliente], max_length = 300)
    telefono = models.CharField(blank= True, validators=[numero_telefono], max_length=20)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    # Relaciones de entidad
    direccion = models.ManyToManyField("users.Direcciones", related_name="direcciones")
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        dirs_str = ""
        dirs = list(self.direccion.all())
        if len(dirs) == 0:
            return f"{self.nombre} {self.ap_paterno} {self.ap_materno}"
            
        dirs_str += f"{dirs[0].__str__()}"
        for dir in dirs[1:]:
            dirs_str += f"{dir.__str__()}"
        return f"Dirección: {dirs_str}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()

class Direcciones(models.Model):
    
    calle = models.CharField(max_length = 60,null=False)
    numero_lt = models.CharField(max_length = 5,null=False)
    numero_mz = models.CharField(max_length = 5,null=False)
    numero_interior = models.CharField(blank = True, max_length = 5)
    colonia = models.CharField(max_length = 40,null=False)
    delegacion = models.CharField(max_length = 20,null=False)
    cp = models.CharField(max_length = 10, null=False)
    
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


class Repartidor(models.Model):
    """Modelo para la BD de un repartidor"""
    nombre = models.CharField(max_length = 80)
    ap_paterno = models.CharField(max_length = 110)
    ap_materno = models.CharField(blank = True, max_length = 110)
    correo = models.EmailField(validators=[unique_email_repartidor], max_length = 300)
    telefono = models.CharField(validators=[numero_telefono], max_length=20)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.nombre} {self.ap_paterno} {self.ap_materno}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
    

class Admin(models.Model):
    """Modelo para la BD de un cliente"""
    nombre = models.CharField(max_length = 80)
    ap_paterno = models.CharField(max_length = 110)
    ap_materno = models.CharField(blank = True, max_length = 110)
    correo = models.EmailField(max_length = 300)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.name} {self.ap_paterno} {self.ap_materno} \n {self.correo}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()


class LoginForm(ModelForm):
    """Define un formulario para iniciar Sesión"""
    class Meta:
        model = Cliente
        fields = ['correo']

class ClienteForm(ModelForm):
    """Define un formulario para crear Cliente"""
    class Meta:
        model = Cliente
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']
        labels = {
            'nombre': ('Nombre'),
            'ap_paterno': ('Apellido Paterno'),
            'ap_materno': ('Apellido Materno*'),
            'correo': ('Correo electrónico'),
            'telefono': ('Número de teléfono*')
        }

class RepartidorForm(ModelForm):
    """Define un formulario para crear Repartidor"""
    class Meta:
        model = Repartidor
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']
        labels = {
            'nombre': ('Nombre'),
            'ap_paterno': ('Apellido Paterno'),
            'ap_materno': ('Apellido Materno*'),
            'correo': ('Correo electrónico'),
            'telefono': ('Número de teléfono')
        }
