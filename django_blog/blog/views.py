from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class HomeView(CreateView):
    pass

class RegisterView(CreateView):
    form_class = UserCreationForm
    
    success_url = reverse_lazy('login')
    template_name = 'blog/registration/signup.html'

class PostsView(CreateView):
    pass
