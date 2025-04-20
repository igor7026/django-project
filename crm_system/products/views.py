from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product


# Create your views here.
class ProductsListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'

class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'

class ProductsCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'cost']
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products-list')

class ProductsUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'cost']
    template_name = 'products/products-edit.html'
    success_url = reverse_lazy('products:products-list')

class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products-list')






