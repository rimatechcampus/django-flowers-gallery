from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import *


class FlowersList(ListView):
    model = Flower
    template_name = 'home.html'
    context_object_name = 'flowers'
    paginate_by = 4


class FlowerDetailView(DetailView):
    model = Flower
    template_name = 'detail.html'
    context_object_name = 'flower'
