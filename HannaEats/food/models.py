from django.forms import ModelForm
from django.db import models
from django.utils.translation import gettext_lazy as _


def direccion_imagenes_comida(selfie, filename):
    """Obtiene el directorio donde se desea guardar imagenes y nombre del archivo"""
    return f"comida/fotos/{selfie.name}{selfie.id}"

def unique_name(value):
    """Verifica que un Charfield sólo contenga números """
    for e in value:
        if(e in value):
            raise ValidationError(
                _('%(value)s Ya existe en la base de datos'),
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
    
    def __str__(selfie):
        """Obtener represencacion como cadena"""
        return f"{selfie.name} por {selfie.precio}"

    def __repr__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.__str__()
    

class Categoria(models.Model):
    """Modelo para la BD de una categoria"""
    name = models.CharField(validators=[unique_name], max_length=120)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    # Relaciones de entidad
    alimentos = models.ManyToManyField("food.Alimento", related_name="miembros")
    
    def __str__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.name

    def __repr__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.__str__()
    

class OrdenComida(models.Model):
    """Modelo para la BD de una orden de comida"""
    estatus = models.IntegerField()
    id_cliente = models.ForeignKey('users.Cliente', on_delete=models.CASCADE)
    id_repartidor = models.ForeignKey('users.Repartidor', on_delete=models.CASCADE)
    #Nota: el atributo Numero Orden de la entidad lo manejaremos como ID
    
    # Relaciones de entidad
    alimentos = models.ManyToManyField("food.Alimento", related_name="articulos")
    
    def __str__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.id

    def __repr__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.__str__()
    
    
class CarritoDeCompras(models.Model):
    """Modelo para la BD de un carrito de compras"""
    subtotal = models.IntegerField()
    #Falta lidiar con el Alimento[]
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    def __str__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.name

    def __repr__(selfie):
        """Obtener represencacion como cadena"""
        return selfie.__str__()
