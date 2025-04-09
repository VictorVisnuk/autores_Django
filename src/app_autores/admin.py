from django.contrib import admin
from . import models

# Register your models here.



class AutoresAdmin(admin.ModelAdmin):
    list_display = ["nombre", "nacionalidad", "fecha_nacimiento", "fecha_fallecimiento", "activo", "creado","modificado"]
    list_filter = ["activo", "nacionalidad","creado","modificado"]
    search_fields = ["nombre","nacionalidad"]
    
admin.site.register(models.Autores, AutoresAdmin)