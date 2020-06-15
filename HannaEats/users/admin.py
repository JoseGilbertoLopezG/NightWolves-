from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import ClienteForm, AccountModifyForm
from .models import Account, Direcciones

class AccountAdmin(UserAdmin):
    add_form = ClienteForm
    form = AccountModifyForm
    model = Account
    
    fieldsets = (
        (None, {'fields': ('correo', 'password', "tipo")}),
        ('Datos', {'fields': ('nombre',"ap_paterno","ap_materno","telefono")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    
    list_display = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']
    ordering = ["tipo", 'nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']

admin.site.register(Account, AccountAdmin)
admin.site.register(Direcciones)
