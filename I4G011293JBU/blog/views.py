from msilib.schema import ListView
from pyexpat import model
from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DetailView
from .models import Post

# Create your views here.
def home(request) :
    return render(request, "home.html", {});

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["__all__"]
    success_url: reverse_lazy("blog.all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = ["__all__"]
    success_url: reverse_lazy("blog.all")

class PostDeleteView(UpdateView):
    model = Post
    fields = ["__all__"]
    success_url: reverse_lazy("blog.all")