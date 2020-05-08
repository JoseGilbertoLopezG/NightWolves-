from django.shortcuts import render, redirect
from django.views import View


class Home(View):    
    template = "inicio.html"

    def get(self, request):
        return render(request, self.template)
