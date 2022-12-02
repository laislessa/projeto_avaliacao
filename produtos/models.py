from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=255)
    def __str__(self) -> str:
            return self.categoria


class Produto(models.Model):
    nome = models.CharField(max_length= 255)
    preco = models.FloatField()
    categorias = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
   