from django.forms import ModelForm
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def direccion_imagenes_comida(self, filename):
    """Obtiene el directorio donde se desea guardar imagenes y nombre del archivo"""
    return f"food/images/{self.nombre}_{self.id}.png"

def unique_status(value):
    """Verifica que un status no exista en la tabla"""
    registered_stati = Status.objects.all()
    for e in registered_stati:
        if(e == value):
            raise ValidationError(
                _('%(value)s Ya existe en la base de datos'),
                code='requiredToBeUnique',
                params={'value': value},
                )

def numeric(value):
    """Verifica que un Charfield sólo contenga números"""
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
        if(e > '5' and e < '0'):
            raise ValidationError(
                _('%(value)s La calificación tiene que ser un número entero de estrellas entre 1 y 5'),
                code='invalidRating',
                params={'value': value},
                )

class Alimento(models.Model):
    """Modelo para la BD de un alimento"""
    nombre = models.CharField(max_length=120,unique=True, error_messages={'required':'Este campo es obligatorio', "max_length":"La longitud máxima es de 120 caracteres", "unique":'Un alimento con este nombre ya existe'})
    descripcion = models.CharField( max_length=200, error_messages={'required':'Este campo es obligatorio', "max_length":"La longitud máxima es de 200 caracteres"})
    precio = models.FloatField(error_messages={'required':'Este campo es obligatorio', "invalid":"Tienes que proporcionar un número (puede tener decimales)"})
    foto = models.ImageField(blank=True, null=True, upload_to=direccion_imagenes_comida)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    # Relaciones de entidad
    categoria = models.ForeignKey("food.Categoria",on_delete=models.CASCADE)
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.nombre} - {self.descripcion} por ${self.precio}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
    

class Categoria(models.Model):
    """Modelo para la BD de una categoria"""
    nombre = models.CharField(max_length=120,unique=True, error_messages={'required':'Este campo es obligatorio', "max_length":"La longitud máxima es de 120 caracteres", "unique":'Una categoria con este nombre ya existe'})
    imagen = models.ImageField(blank=True, null=True, upload_to=direccion_imagenes_comida)
    #Nota: el atributo ID de la entidad existe por defecto en Django
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return self.nombre

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()    

class OrdenComida(models.Model):
    """Modelo para la BD de una orden de comida"""
    TIPOS_DE_STATUS = ( 
        (1, "listo_para_entrega"), 
        (2, "en_entrega"), 
        (3, "entregado"),
        (4, "carrito")
    )
    status = models.ForeignKey('food.Status', on_delete=models.CASCADE)
    id_cliente = models.ForeignKey('users.Account',  
                                   related_name="cliente", on_delete=models.CASCADE)
    id_repartidor = models.ForeignKey('users.Account', blank=True, null=True,
                                    related_name="repartidor",
                                    on_delete=models.CASCADE)
    calificacion = models.IntegerField(validators=[grade], null=True, blank=True)
    #Nota: el atributo Numero Orden de la entidad lo manejaremos como ID
    
    # Relaciones de entidad
    alimentos = models.ManyToManyField("food.Alimento", related_name="articulos",through="food.CantidadAlimento", blank=True)
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        ''' a = 0
        for i in alimentos:
            a += i.cantidad * i.alimento.precio '''
        return f"Orden {self.id} por $" +" para {self.id_cliente}" 

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()

class Status(models.Model):
    """Modelo auxiliar para una orden de comida"""
    status = models.CharField(validators=[unique_status], max_length=30)
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.status}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
    
class CantidadAlimento(models.Model):
    """Modelo auxiliar para una orden de comida"""
    cantidad = models.IntegerField()
    
    # Relaciones de entidad
    orden = models.ForeignKey('food.OrdenComida', on_delete=models.CASCADE, related_name='orden')
    alimento = models.ForeignKey('food.Alimento', on_delete=models.CASCADE, related_name='cantidad_alimento')
    ## initial=5
    
    def __str__(self):
        """Obtener represencacion como cadena"""
        return f"{self.alimento}                      x{self.cantidad}"

    def __repr__(self):
        """Obtener represencacion como cadena"""
        return self.__str__()
