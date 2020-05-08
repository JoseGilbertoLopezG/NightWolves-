from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import ClienteForm, AccountModifyForm
from .models import Account, Direcciones

admin.site.register(Account)
admin.site.register(Direcciones)
