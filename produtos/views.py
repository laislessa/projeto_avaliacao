from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from produtos.models import Produto,Categoria



class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["nome","preco", "categorias"]
    template_name = 'produtos/produto_form.html'
    success_url = "/produtos/"

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ["nome","preco","categorias"]
    template_name = 'produtos/produto_form.html'
    success_url ="/produtos/"

class ProdutoDeleteView(DeleteView):
    model = Produto
    fields = ["nome","preco"," categorias"]
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = "/produtos/"

class ProdutoDetailView(DetailView):
   model = Produto

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ["categoria"]
    template_name = 'produtos/categoria_formulario.html'
    success_url = "/categorias/"


class ProdutoListView(ListView):
    model = Produto
    context_object_name = "produtos"


class CategoriaListView(ListView):
    model = Categoria
    context_object_name = "categorias"
    template_name = 'produtos/categoria_list.html'

class OpcoesListView(ListView):
    model = Categoria
    template_name = 'produtos/base.html'