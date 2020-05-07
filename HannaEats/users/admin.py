from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cliente)
admin.site.register(Repartidor)
admin.site.register(Admin)
admin.site.register(Direcciones)
