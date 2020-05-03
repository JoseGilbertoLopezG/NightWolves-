from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Models
from django.db import models
from users.models import Cliente
from users.models import ClienteForm
from users.models import Direcciones
from .models import OrdenComida
from .models import Status
from .models import Alimento
from .models import CantidadAlimento

class IndexFood(View):
    
    template = "food/index.html"

    def get(self, request):
        return render(request, self.template)
    
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
    

class AllStatus(UpdateView):
    
    model = OrdenComida
    fields = ['status']
    template_name = "food/status.html"
    success_url = '/'
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

''' Views para calificacion de la orden '''

class OneStar(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "food/calification.html"
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
        return redirect("/orders")
    
class TwoStars(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "food/calification.html"
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
        return redirect("/orders")

class ThreeStars(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "food/calification.html"
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
        return redirect("/orders")
    
class FourStars(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "food/calification.html"
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
        return redirect("/orders")
    
class FiveStars(UpdateView):
    model = OrdenComida
    fields = ['calificacion']
    template_name = "food/calification.html"
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
        return redirect("/orders")

''' Views para cambiar el estado de orden '''

''' View para cambiar a recibida '''
class ChangeStatusToReceived(UpdateView):
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
        to_update = OrdenComida.objects.filter(id=pk).update(status=1)
        return redirect("/orders")
    
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
        return redirect("/orders")
    
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
        return redirect("/orders")

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
        return redirect("/orders")

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
        return redirect("/orders")

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
        return redirect("/orders")
    
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
        return redirect("/orders")