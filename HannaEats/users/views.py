from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

#Models
from django.db import models
from .models import Cliente
from .models import ClienteForm
from .models import Direcciones

# Forms
from users.forms import DirectionsForm

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
    
class AllDir(View):
    
    template = "users/dirs.html"

    def get(self, request):
        """GET method."""
        dirs = Direcciones.objects.all()
        
        dirs_id = request.GET.get("to_see", 1)
        
        dirs_to_see = Direcciones.objects.filter(id=dirs_id)
                
        #if dirs_to_see.count() == 0:
        #    to_see = Direcciones.objects.first()
        #else:
        #to_see = dirs_to_see.first() , "to_see": to_see

        context = {"dirs": dirs}
        return render(request, self.template)