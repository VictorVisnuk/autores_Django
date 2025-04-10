from django.db import models
from app_autores.models import Autores
# Create your models here.

class Frases(models.Model):
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE, related_name="frases")
    frase = models.TextField()
    comentarios = models.CharField(max_length=100, null=True)
    fecha_frase = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    visible = models.BooleanField()

    def __str__(self):
        return F"""{self.frase}\n{self.autor}"""