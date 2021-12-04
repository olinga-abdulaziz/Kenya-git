from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class home(generic.ListView):
    model=Post  
    ordering="-id"
    context_object_name='posts'
    template_name='baseapp/home.html'
   
class AddView(generic.CreateView):
    model=Post
    fields="__all__"
    template_name='baseapp/addpost.html'
    success_url=reverse_lazy('home')




