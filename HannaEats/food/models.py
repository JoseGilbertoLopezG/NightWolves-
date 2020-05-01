from django.forms import ModelForm
from django.db import models
from django.utils.translation import gettext_lazy as _


def direccion_imagenes_comida(self, filename):
    """Obtiene el directorio donde se desea guardar imagenes y nombre del archivo"""
    return f"comida/fotos/{self.name}{self.id}"

def unique_name(value):
    """Verifica que un Charfield sólo contenga números """
    for e in value:
        if(e in value):
            raise ValidationError(
                _('%(value)s Ya existe en la base de datos'),
                code='existValue',
                params={'value': value},
                )

def numero(value):
    """Verifica que un Charfield sólo contenga números """
    for e in value:
        if(e == ' ' or (e >= '0' and e <= '9')):
            raise ValidationError(
                _('%(value)s no es un número de teléfono válido'),
                code='numbersOnly',
                params={'value': value},
                )

def grade(value):
    """Verifica que un Charfield sólo contenga números """
    for e in value:
        if(e > 5 and e < 0):
            raise ValidationError(
                _('%(value)s Calificacione mayor de 5 estrellas no se puede'),
                code='existValue',
                params={'value': value},
                )

class Alimento(models.Model):
    """Modelo para la BD de un alimento"""
    nombre = models.CharField(validators=[unique_name], max_length=120)
    descripcion = models.CharField(validators=[unique_name], max_length=200)
    precio = models.CharField(validators=[unique_name], max_length=200)
    foto = models.ImageField(blank=True, null=True, upload_to=direccion_imagenes_comida)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    # Relaciones de entidad
    categoria = models.ManyToManyField("food.Categoria", related_name="clasificacion")
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.descripcion} por ${self.precio}.00"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
    

class Categoria(models.Model):
    """Modelo para la BD de una categoria"""
    name = models.CharField(validators=[unique_name], max_length=120)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    # Relaciones de entidad
    alimentos = models.ManyToManyField("food.Alimento", related_name="miembros")
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return self.name

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
    

class OrdenComida(models.Model):
    """Modelo para la BD de una orden de comida"""
    status = models.ForeignKey('food.Status', on_delete=models.CASCADE)
    id_cliente = models.ForeignKey('users.Cliente', on_delete=models.CASCADE)
    id_repartidor = models.ForeignKey('users.Repartidor', on_delete=models.CASCADE)
    calificacion = models.IntegerField(validators=[grade], null=True)
    #Nota: el atributo Numero Orden de la entidad lo manejaremos como ID
    
    # Relaciones de entidad
    alimentos = models.ManyToManyField("food.Alimento", related_name="articulos",through="food.CantidadAlimento")
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.id_cliente}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()

class Status(models.Model):
    """Modelo para la BD de una orden de comida"""
    status = models.CharField(validators=[unique_name], max_length=120)
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.status}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
    
class CantidadAlimento(models.Model):
    """Modelo para la BD de una orden de comida"""
    orden = models.ForeignKey('food.OrdenComida', on_delete=models.CASCADE, related_name='cantidad_alimento')
    alimento = models.ForeignKey('food.Alimento', on_delete=models.CASCADE, related_name='cantidad_alimento')
    cantidad = models.CharField(validators=[numero], max_length=5)
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.alimento}                      x{self.cantidad}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
    
    
class CarritoDeCompras(models.Model):
    """Modelo para la BD de un carrito de compras"""
    subtotal = models.IntegerField()
    #Falta lidiar con el Alimento[]
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return self.name

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
