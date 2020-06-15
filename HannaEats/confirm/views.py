from django.shortcuts import render
from HannaEats.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import Confirm

# Create your views here.

class ConfirmEmail(View):
    
    template = "confirm/index.html"

    def get(self, request):
        """Render add artist form."""
        form = Confirm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        sub = Confirm(request.POST)
        subject = 'Bienvienido A HannaEats'
        message = 'Esperamos que su experiencia con nosotros sea buena'
        recepient = str(sub['Email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'confirm/success.html', {'recepient': recepient})
