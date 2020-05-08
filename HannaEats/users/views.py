from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages

#Models
from django.db import models
from .models import Direcciones
from food.models import OrdenComida

# Forms
from .forms import ClienteForm
from .forms import RepartidorForm
from .forms import AccountLoginForm
from .forms import DirectionsForm


class CreateClient(View):
    """Página para crear una cuenta de Cliente"""
    
    template = "users/create_client.html"
    
    def get(selfie, request):
        form = ClienteForm()
        context = {'form': form}
        return render(request, selfie.template, context)
        
    def post(selfie, request):
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            form.instance.tipo ='3'
            form.save()
            messages.info(request, 'Los datos fueron guardados.\nLa cuenta será borrada, si no se verifica el correo electónico siguiendo el link enviado, en 24hrs')
            return render( request, selfie.template, {'form': form,
                                                      "contrib_messages": messages})
        else:
            template = selfie.template
            return render( request, selfie.template, {'form': form})
    

class CreateAccount(View):
    """Página para crear una cuenta de Repartidor"""
    
    template = "users/create_account.html"
    
    def get(selfie, request):
        form = RepartidorForm()
        context = {'form': form}
        return render(request, selfie.template, context)
        
    def post(selfie, request):
        form = RepartidorForm(request.POST)
        
        if form.is_valid():
            form.instance.tipo ='2'
            form.save()
            messages.info(request, 'Los datos fueron guardados.\nLa cuenta será borrada, si no se verifica el correo electónico siguiendo el link enviado, en 24hrs')
            return render( request, selfie.template, {'form': form,
                                                      "contrib_messages": messages})
        else:
            template = selfie.template
            return render( request, selfie.template, {'form': form})
        

class Login(View):
    """Página de inicio de sesion"""
    template = "users/login.html"

    def get(selfie, request):
        form = AccountLoginForm()
        context = {"form": form}
        return render(request, selfie.template, context)

    def post(selfie, request):
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd.get('username'), password=cd.get('password') )
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.info(request, 'Los datos no son correctos. Intenta de nuevo')
                return render(request, selfie.template, {'form': form,
                                                      "contrib_messages": messages})
        else:
            messages.info(request, 'Asegurate de llenar los campos como se pide')
            return render(request, selfie.template, {'form': form,
                                                      "contrib_messages": messages})
 
class Logout(View):
    """Página de inicio de sesion"""
    template = "users/login.html"
    
    def get(selfie, request):
        logout(request)
        return redirect('/')


class AddDir(View):
    """New User Sign Up."""

    template = "users/add_dir.html"

    def get(self, request):
        form = DirectionsForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        form = DirectionsForm(request.POST)

        if not form.is_valid():
            context = {"form": form}
            return DirectionsForm(request, self.template, context)

        Direcciones.objects.create(
            calle = form.cleaned_data["calle"],
            numero_lt = form.cleaned_data["numero_lt"],
            numero_mz = form.cleaned_data["numero_mz"],
            colonia = form.cleaned_data["colonia"],
            delegacion = form.cleaned_data["delegacion"],
            cp = form.cleaned_data["cp"]
        )
        #return HttpResponse("<h1>User Created!</h1>")
        return redirect("/")
    

class UpdateDir(UpdateView):
    model = Direcciones
    fields = '__all__'
    template_name = "users/upd_dir.html"
    success_url = '/'
    title = "Editar direccion"
    labels = {
            'calle': ('Calle'),
            'numero_lt': ('Lt'),
            'numero_mz': ('Mz'),
            'numero_interior': ('Num. Interior*'),
            'colonia': ('Colonia'),
            'delegacion': ('Delegación'),
            'cp' : ('Código Postal'),
        }
        
    
    
class DelDir(DeleteView):
    model = Direcciones
    template_name = "users/del_dir.html"
    success_url = '/users/all-directions'
    title = 'Borrar Direcciones'
    
class AllDir(View):
    
    template = "users/dirs.html"

    def get(self, request):
        """GET method."""
        dirs = Direcciones.objects.all()
        
        dirs_id = request.GET.get("to_see", 1)
        
        dirs_to_see = Direcciones.objects.filter(id=dirs_id)
                
        if dirs_to_see.count() == 0:
            to_see = Direcciones.objects.first()

        else:
            to_see = dirs_to_see.first()
            
        context = {"dirs": dirs,"to_see": to_see}
        return render(request, self.template, context)
    

''' Views para calificacion de la orden '''

class OneStar(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "users/calification.html"
    success_url = '/'
    title = "Editar direccion"
    
    def get(self, request, pk):
        """GET method."""
        orders = OrdenComida.objects.all()
        orders_id = request.GET.get("to_see", 1)
        orders_to_see = OrdenComida.objects.filter(id=orders_id)
                
        if orders_to_see.count() == 0:
            to_see = OrdenComida.objects.first()
        else:
            to_see = orders_to_see.first()
            
        context = {"orders": orders,"to_see": to_see}
        return render(request, self.template_name, context)

    def post(self,request,pk):
        to_update = OrdenComida.objects.filter(id=pk).update(calificacion=1)
        return redirect("/")
    
class TwoStars(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "users/calification.html"
    success_url = '/'
    title = "Editar direccion"
    
    def get(self, request, pk):
        """GET method."""
        orders = OrdenComida.objects.all()
        orders_id = request.GET.get("to_see", 1)
        orders_to_see = OrdenComida.objects.filter(id=orders_id)
                
        if orders_to_see.count() == 0:
            to_see = OrdenComida.objects.first()
        else:
            to_see = orders_to_see.first()
            
        context = {"orders": orders,"to_see": to_see}
        return render(request, self.template_name, context)

    def post(self,request,pk):
        to_update = OrdenComida.objects.filter(id=pk).update(calificacion=2)
        return redirect("/")

class ThreeStars(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "users/calification.html"
    success_url = '/'
    title = "Editar direccion"
    
    def get(self, request, pk):
        """GET method."""
        orders = OrdenComida.objects.all()
        orders_id = request.GET.get("to_see", 1)
        orders_to_see = OrdenComida.objects.filter(id=orders_id)
                
        if orders_to_see.count() == 0:
            to_see = OrdenComida.objects.first()
        else:
            to_see = orders_to_see.first()
            
        context = {"orders": orders,"to_see": to_see}
        return render(request, self.template_name, context)

    def post(self,request,pk):
        to_update = OrdenComida.objects.filter(id=pk).update(calificacion=3)
        return redirect("/")
    
class FourStars(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "users/calification.html"
    success_url = '/'
    title = "Editar direccion"
    
    def get(self, request, pk):
        """GET method."""
        orders = OrdenComida.objects.all()
        orders_id = request.GET.get("to_see", 1)
        orders_to_see = OrdenComida.objects.filter(id=orders_id)
                
        if orders_to_see.count() == 0:
            to_see = OrdenComida.objects.first()
        else:
            to_see = orders_to_see.first()
            
        context = {"orders": orders,"to_see": to_see}
        return render(request, self.template_name, context)

    def post(self,request,pk):
        to_update = OrdenComida.objects.filter(id=pk).update(calificacion=4)
        return redirect("/")
    
class FiveStars(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "users/calification.html"
    success_url = '/'
    title = "Editar direccion"
    
    def get(self, request, pk):
        """GET method."""
        orders = OrdenComida.objects.all()
        orders_id = request.GET.get("to_see", 1)
        orders_to_see = OrdenComida.objects.filter(id=orders_id)
                
        if orders_to_see.count() == 0:
            to_see = OrdenComida.objects.first()
        else:
            to_see = orders_to_see.first()
            
        context = {"orders": orders,"to_see": to_see}
        return render(request, self.template_name, context)

    def post(self,request,pk):
        to_update = OrdenComida.objects.filter(id=pk).update(calificacion=5)
        return redirect("/")
    
class CartAdd(UpdateView):
    template_name = "users/cart.html"
    
class CartDelete(UpdateView):
    template_name = "users/cart.html"
    
class CartContents(UpdateView):
    template_name = "users/cart.html"
    
class CartCheckout(UpdateView):
    template_name = "users/cart.html"
