from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib import messages

#Email
from HannaEats.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

#Models
from django.db import models
from .models import Direcciones
from .models import Account
from food.models import OrdenComida

# Forms
from .forms import ClienteForm
from .forms import RepartidorForm
from .forms import AccountLoginForm
from .forms import DirectionsForm

''' View para cambiar a recibida '''

class VerifyCount(UpdateView):
    model = Account
    fields = ['is_active']
    template_name = "users/verify.html"
    success_url = '/'
    title = "Activar cuenta"
    
    def get(self, request, correo):
        """GET method."""
        count = Account.objects.all()
        count_id = request.GET.get("to_see", 1)
        count_to_see = Account.objects.filter(id=count_id)
                
        if count_to_see.count() == 0:
            to_see = Account.objects.first()
        else:
            to_see = count_to_see.first()
            
        context = {"count": count,"to_see": to_see}
        return render(request, self.template_name, context)

    def post(self,request,correo):
        to_update = Account.objects.filter(correo=correo).update(is_active=True)
        return redirect("/")


class CreateClient(View):
    """Página para crear una cuenta de Cliente"""
    
    template = "users/create_client.html"
    
    def cut(self,s):
        last = ""
        for c in s:
            if not (c == "@"):
                last+= c
            else:
                break
        return last
    
    def get(self, request):
        form = ClienteForm()
        context = {'form': form}
        return render(request, self.template, context)
        
    def post(self, request):
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            sub = ClienteForm(request.POST)
            
            #link = str(sub['correo'].value())
            
            subject = 'Bienvienido A HannaEats'
            message = '¡Bienvenido '+str(sub['nombre'].value())+'!\nEsperamos que su experiencia con nosotros sea buena.\nVerifica tu Cuenta:\n\n'+'http://localhost:8000/user/verificar/'+str(sub['correo'].value())+'\n'
            recepient = str(sub['correo'].value())
            from_email = 'Hanna Eats'
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            
            form.instance.is_active = False
            form.instance.tipo ='3'
            form.save()
            messages.info(request, 'Los datos fueron guardados.\nLa cuenta será borrada, si no se verifica el correo electónico siguiendo el link enviado, en 24hrs')
            return render( request, 'confirm/success.html', {'form': form,
                                                      "contrib_messages": messages,
                                                      'recepient': recepient})
        else:
            template = self.template
            return render( request, self.template, {'form': form})
    

class CreateAccount(View):
    """Página para crear una cuenta de Repartidor"""
    
    template = "users/create_account.html"
    
    def cut(self,s):
        last = ""
        for c in s:
            if not (c == "@"):
                last+= c
            else:
                break
        return last
    
    def get(self, request):
        form = RepartidorForm()
        context = {'form': form}
        return render(request, self.template, context)
        
    def post(self, request):
        form = RepartidorForm(request.POST)
        
        if form.is_valid():
            sub = RepartidorForm(request.POST)
            
            subject = 'Bienvienido A HannaEats'
            message = '¡Bienvenido '+str(sub['nombre'].value())+'!\nEsperamos que su experiencia con nosotros sea buena.\nVerifica tu Cuenta:\n\n'+'http://localhost:8000/user/verificar/'+str(sub['correo'].value())+'\n'
            recepient = str(sub['correo'].value())
            from_email = 'Hanna Eats'
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            
            form.instance.is_active = False
            
            form.instance.tipo ='2'
            form.save()
            messages.info(request, 'Los datos fueron guardados.\nLa cuenta será borrada, si no se verifica el correo electónico siguiendo el link enviado, en 24hrs')
            return render( request, 'confirm/success.html', {'form': form,
                                                      "contrib_messages": messages,
                                                        'recepient': recepient})
        else:
            template = self.template
            return render( request, self.template, {'form': form})
        

class Login(View):
    """Página de inicio de sesion"""
    
    template = "users/login.html"

    def get(self, request):
        form = AccountLoginForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd.get('username'), password=cd.get('password') )
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.info(request, 
                              'Los datos no son correctos. Intenta de nuevo')
                return render(request, self.template, {'form': form,
                                                "contrib_messages":messages})
        else:
            messages.info(request, 'Asegurate de llenar los campos como se pide')
            return render(request, self.template, {'form': form,
                                                "contrib_messages":messages})
 
class Logout(View):
    """Página de inicio de sesion"""
    template = "users/login.html"
    
    def get(self, request):
        logout(request)
        return redirect('/')

@method_decorator(login_required, name='dispatch')
class AddDir(View):
    """New User Sign Up."""

    template = "users/add_dir.html"

    def get(self, request,pk):
        form = DirectionsForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request,pk):
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
        ).direccion.add(pk)
        
        #return HttpResponse("<h1>User Created!</h1>")
        return redirect("/")
    
@method_decorator(login_required, name='dispatch')
class UpdateDir(UpdateView):
    model = Direcciones
    fields = ['calle','numero_lt','numero_mz','numero_interior','colonia','delegacion','cp']
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
    
    ''' def get(self, request, pk):
        dir = Direcciones.objects.filter(id=pk).get()
        context = {"pk":dir}
        return render(request, self.template_name, context) '''
    
@method_decorator(login_required, name='dispatch')  
class DelDir(DeleteView):
    model = Direcciones
    template_name = "users/del_dir.html"
    success_url = '/users/all-directions'
    title = 'Borrar Direcciones'

@method_decorator(login_required, name='dispatch')  
class AllDir(View):
    
    template = "users/dirs.html"

    def get(self, request, pk):
        """GET method."""
        
        cuentas = Direcciones.objects.filter(direccion=pk).all()
        
        dirs = Direcciones.objects.filter(direccion=pk).all()
        dirs_id = request.GET.get("to_see", 1)
        dirs_to_see = Direcciones.objects.filter(id=dirs_id)
                
        if dirs_to_see.count() == 0:
            to_see = Direcciones.objects.first()

        else:
            to_see = dirs_to_see.first()
            
        context = {"dirs": dirs,"to_see": to_see,"pk":pk,"cuentas":cuentas}
        return render(request, self.template, context)
    

''' Views para calificacion de la orden '''

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')   
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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')    
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

@method_decorator(login_required, name='dispatch')    
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
