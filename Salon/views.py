from django.shortcuts import render
from django.views.generic import ListView

from .models import *


# Create your views here.

class CarsList(ListView):
    model = Cars
    template_name = 'salon/index.html'
    context_object_name = 'cars'
    extra_context = {
        'title': 'Auto Dealership',
        'dachas': Cars.objects.all()
    }
