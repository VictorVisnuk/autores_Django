from django.db import models

# Create your models here.

class Autores(models.Model):

    NACIONALIDADES = {
      "Argentina": "Argentina",
    "Boliviana": "Boliviana",
    "Brasileña": "Brasileña",
    "Chilena": "Chilena",
    "Colombiana": "Colombiana",
    "Costarricense": "Costarricense",
    "Cubana": "Cubana",
    "Dominicana": "Dominicana",
    "Ecuatoriana": "Ecuatoriana",
    "Salvadoreña": "Salvadoreña",
    "Guatemalteca": "Guatemalteca",
    "Hondureña": "Hondureña",
    "Mexicana": "Mexicana",
    "Nicaragüense": "Nicaragüense",
    "Panameña": "Panameña",
    "Paraguaya": "Paraguaya",
    "Peruana": "Peruana",
    "Puertorriqueña": "Puertorriqueña",
    "Uruguaya": "Uruguaya",
    "Venezolana": "Venezolana",
    "Española": "Española",
    "Estadounidense": "Estadounidense",
    "Canadiense": "Canadiense",
    "Francesa": "Francesa",
    "Alemana": "Alemana",
    "Italiana": "Italiana",
    "Portuguesa": "Portuguesa",
    "Británica": "Británica",
    "Irlandesa": "Irlandesa",
    "China": "China",
    "Japonesa": "Japonesa",
    "Coreana": "Coreana",
    "India": "India",
    "Rusa": "Rusa",
    "Australiana": "Australiana",
    "Sudafricana": "Sudafricana",
    "Egipcia": "Egipcia",
    "Nigeriana": "Nigeriana",
    "Keniata": "Keniata",
    "Marroquí": "Marroquí"
    }
    nombre = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=20, choices=NACIONALIDADES.items(), default="Argentina")
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return F"[{self.id}] {self.nombre.upper()} ({self.nacionalidad})"
    
    class Meta:
        ordering = ['id']
        verbose_name = "Autores"
        verbose_name_plural = "Autores"