from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.db import models

class IndexFood(View):

    template = "food/index.html"

    def get(self, request):
        return render(request, self.template)