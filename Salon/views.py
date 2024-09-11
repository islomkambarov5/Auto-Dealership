from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


# Create your views here.

class CarsList(ListView):
    model = Cars
    template_name = 'salon/index.html'
    context_object_name = 'cars'
    extra_context = {
        'title': 'Auto Dealership',
        'cars': Cars.objects.all()
    }


class CarDetail(DetailView):
    model = Cars
    template_name = 'salon/index.html'
    context_object_name = 'car_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        car = Cars.objects.get(slug=self.kwargs['slug'])

        context['title'] = 'Car Model Detail - Auto Dealership'
        context['car'] = car

