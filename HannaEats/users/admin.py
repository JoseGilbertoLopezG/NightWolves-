from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import ClienteForm, ClienteModifyForm
from .models import Cliente, Repartidor, Admin, Direcciones

admin.site.register(Cliente)
admin.site.register(Repartidor)
admin.site.register(Admin)
admin.site.register(Direcciones)
