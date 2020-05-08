from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import ClienteForm, AccountModifyForm
from .models import Account, Direcciones

class AccountAdmin(UserAdmin):
    add_form = ClienteForm
    form = AccountModifyForm
    model = Account
    list_display = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']
    ordering = ['nombre', 'ap_paterno', 'ap_materno', 'correo', 'telefono']

admin.site.register(Account, AccountAdmin)
admin.site.register(Direcciones)
