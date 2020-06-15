from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Alimento)
admin.site.register(Categoria)
admin.site.register(Status)
admin.site.register(OrdenComida)
admin.site.register(CantidadAlimento)
