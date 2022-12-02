from django.contrib import admin
from django.urls import path
from produtos.views import ProdutoListView, CategoriaListView ,ProdutoCreateView, ProdutoDetailView, ProdutoUpdateView, ProdutoDeleteView, CategoriaCreateView,OpcoesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', ProdutoListView.as_view()),
    path('categorias/', CategoriaListView.as_view()),
    path('', OpcoesListView.as_view()),
    path('produtos/cadastrar/', ProdutoCreateView.as_view()),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view()),
    path('produtos/atualizar/<int:pk>/', ProdutoUpdateView.as_view()),
    path('produtos/deletar/<int:pk>/', ProdutoDeleteView.as_view()),
    path('categorias/cadastrar/', CategoriaCreateView.as_view())

]
