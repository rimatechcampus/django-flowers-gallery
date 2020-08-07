from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterView(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = 'accounts/login/'
