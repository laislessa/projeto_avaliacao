from django.apps import AppConfig


class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'

class CategoriasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categorias'
