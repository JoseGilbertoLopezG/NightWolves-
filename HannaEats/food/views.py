from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Models
from django.db import models
from users.models import Direcciones
from .models import Status
from .models import Alimento
from .models import Categoria
from .models import CantidadAlimento
from .models import OrdenComida

# Forms
from .forms import FoodForm
from users.forms import ClienteForm
from food.forms import FoodForm
from food.forms import CategoryForm

class IndexFood(View):
    
    template = "food/index.html"

    def get(self, request):
        return render(request, self.template)

class CategoriaVista(View):
    
    template = "food/home_cat.html"

    def get(self, request):
        """GET method."""
        categorias = Categoria.objects.all()
        context = {"categorias": categorias}
        return render(request, self.template, context)
    
class ComidaVista(View):

    template = "food/categoria_comida.html"

    def get(self, request, name):
        """GET method."""
        cat = name.capitalize()
        id = Categoria.objects.filter(nombre = name.capitalize()).first()
        foods = Alimento.objects.filter(categoria_id = id)
        context = {"foods": foods,"cat":cat}
        return render(request, self.template, context)
    
class AllOrders(View):
    
    template = "food/orders.html"

    def get(self, request):
        """GET method."""
        orders = OrdenComida.objects.all()
        orders_id = request.GET.get("to_see", 1)
        orders_to_see = OrdenComida.objects.filter(id=orders_id)
                
        if orders_to_see.count() == 0:
            to_see = OrdenComida.objects.first()
        else:
            to_see = orders_to_see.first()
            
        foods = Alimento.objects.all()
        foods_id = request.GET.get("to_see", 1)
        foods_to_see = Alimento.objects.filter(id=foods_id)
                
        if foods_to_see.count() == 0:
            to_eat = Alimento.objects.first()
        else:
            to_eat = foods_to_see.first()
            
        cants = CantidadAlimento.objects.all()
        cants_id = request.GET.get("to_see", 1)
        cants_to_see = CantidadAlimento.objects.filter(id=cants_id)
                
        if cants_to_see.count() == 0:
            to_count = CantidadAlimento.objects.first()
        else:
            to_count = cants_to_see.first()
            
        context = {"orders": orders,"to_see": to_see,"foods": foods,"to_eat": to_eat,"cants":cants, "to_count":to_count}
        return render(request, self.template, context)
    
""" Views referentes a los alimentos """

class AllFood(View):
    
    template = "food/food.html"

    def get(self, request):
        """GET method."""
        foods = Alimento.objects.all()
        foods_id = request.GET.get("to_see", 1)
        foods_to_see = Alimento.objects.filter(id=foods_id)
                
        if foods_to_see.count() == 0:
            to_eat = Alimento.objects.first()
        else:
            to_eat = foods_to_see.first()
        context = {"foods": foods,"to_eat": to_eat}
        return render(request, self.template, context)
    
class AddFood(View):

    template = "food/add_food.html"

    def get(self, request):
        """Render add artist form."""
        form = FoodForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        form = FoodForm(request.POST, request.FILES)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        Alimento.objects.create(
            nombre=form.cleaned_data["nombre"],
            descripcion=form.cleaned_data["descripcion"],
            precio=form.cleaned_data["precio"],
            foto=form.cleaned_data["foto"],
            categoria=form.cleaned_data["categoria"]
        )
        return redirect("/food/all")


class UpdateFood(UpdateView):
    model = Alimento
    fields = '__all__'
    template_name = "food/updt_food.html"
    success_url = '/food/all'
    
    
class DelFood(DeleteView):
    model = Alimento
    template_name = "food/del_food.html"
    success_url = '/food/all'
    
""" Views referentes a las categorias """

class AllCategorys(View):
    
    template = "food/categoria.html"

    def get(self, request):
        """GET method."""            
        categorias = Categoria.objects.all()
        categorias_id = request.GET.get("to_see", 1)
        categorias_to_see = Categoria.objects.filter(id=categorias_id)
                
        if categorias_to_see.count() == 0:
            to_see = Categoria.objects.first()
        else:
            to_see = categorias_to_see.first()
            
        context = {"categorias":categorias,"to_see":to_see}
        return render(request, self.template, context)
    
class AddCategory(View):

    template = "food/add_categ.html"

    def get(self, request):
        """Render add artist form."""
        form = CategoryForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        Categoria.objects.create(
            nombre=form.cleaned_data["nombre"],
            imagen=form.cleaned_data["imagen"],
        )
        return redirect("/food/category")


class UpdateCategory(UpdateView):
    model = Categoria
    fields = '__all__'
    template_name = "food/updt_categ.html"
    success_url = '/'
    
    
class DelCategory(DeleteView):
    model = Categoria
    template_name = "food/del_categ.html"
    success_url = '/food/category'
    
""" Views de los estados de las comidas """

class AllStatus(UpdateView):
    
    model = OrdenComida
    fields = ['status']
    template_name = "food/status.html"
    success_url = '/food/category'
    title = "Editar direccion"
    
    def get(self, request, pk):
        """GET method."""
        orders = OrdenComida.objects.all()
        orders_to_see = OrdenComida.objects.filter(id=pk)
                
        if orders_to_see.count() == 0:
            to_see = OrdenComida.objects.first()
        else:
            to_see = orders_to_see.first()
            
        context = {"orders": orders,"to_see": to_see}
        return render(request, self.template_name, context)


''' Views para cambiar el estado de orden '''

''' View para cambiar a recibida '''
class ChangeStatusToReceived(UpdateView):
    model = OrdenComida
    fields = ['status']
    template_name = "food/eachstatus.html"
    success_url = '/food/orders'
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
        to_update = OrdenComida.objects.filter(id=pk).update(status=1)
        return redirect("/food/orders")
    
''' View para cambiar a preparandose '''
    
class ChangeStatusToPrepared(UpdateView):
    model = OrdenComida
    fields = ['status']
    template_name = "food/eachstatus.html"
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
        to_update = OrdenComida.objects.filter(id=pk).update(status=2)
        return redirect("/food/orders")
    
''' View para cambiar a en espera '''
    
class ChangeStatusToWait(UpdateView):
    model = OrdenComida
    fields = ['status']
    template_name = "food/eachstatus.html"
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
        to_update = OrdenComida.objects.filter(id=pk).update(status=3)
        return redirect("/food/orders")

''' View para cambiar a en Camino '''

class ChangeStatusToOnWay(UpdateView):
    model = OrdenComida
    fields = ['status']
    template_name = "food/eachstatus.html"
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
        to_update = OrdenComida.objects.filter(id=pk).update(status=4)
        return redirect("/food/orders")

''' View para cambiar a Entregada '''
    
class ChangeStatusToDelivered(UpdateView):
    model = OrdenComida
    fields = ['status']
    template_name = "food/eachstatus.html"
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
        to_update = OrdenComida.objects.filter(id=pk).update(status=5)
        return redirect("/food/orders")

''' View para cambiar a finalizada ''' 
    
class ChangeStatusToFinalized(UpdateView):
    model = OrdenComida
    fields = ['status']
    template_name = "food/eachstatus.html"
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
        to_update = OrdenComida.objects.filter(id=pk).update(status=6)
        return redirect("/food/orders")
    
''' View para cambiar a cancelada '''

class ChangeStatusToCanceled(UpdateView):
    model = OrdenComida
    fields = ['status']
    template_name = "food/eachstatus.html"
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
        to_update = OrdenComida.objects.filter(id=pk).update(status=7)
        return redirect("/food/orders")
