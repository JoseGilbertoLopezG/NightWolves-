from django.shortcuts import render, redirect
from django.views import View


class Home(View):    
    template = "inicio.html"

    def get(self, request):
        return render(request, self.template)

class MenuSesion(View):    
    template = "menu_sesion.html"

    def get(self, request):
        return render(request, self.template)
