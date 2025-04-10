from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import  CreateView, UpdateView
from .models import Autores

# Create your views here.

def inicial(request=...):
    return render(request, "base.html" )

def presentacion(request=...):
    return render(request, "presentacion.html" )

def listar_autores(request):
    autores = Autores.objects.all()    
    
    return render(request,
                  "app_autores/listar.html",
                  {"autores":autores})
    

def listar_autores_activos(request):
    autores = Autores.objects.filter(activo = True)     
    
    return render(request,
                  "app_autores/listar.html",
                  {"autores":autores})
    

def listar_autores_inactivos(request):
    autores = Autores.objects.filter(activo = False)     
    
    return render(request,
                  "app_autores/listar.html",
                  {"autores":autores})
    

def listar_json(request):
    autores = get_list_or_404(Autores)
    autores_json = serializers.serialize("json", autores)
    return JsonResponse(autores_json, safe=False)

def detalle(request, id):
    autor = get_object_or_404(Autores, id = id)
    
    return render(request,
                  "app_autores/detalle.html",
                  {"autor" : autor})
    
def borrar_autor(request, id):
    autor_a_borrar = get_object_or_404(Autores, id=id)
    autor_a_borrar.delete()
    if autor_a_borrar.activo:
        return HttpResponseRedirect(reverse('app_autores:listar_autores_activos'))
    else:
        return HttpResponseRedirect(reverse('app_autores:listar_autores_inactivos'))
    
def modificar_activo(request, id):
    autor_a_modificar = get_object_or_404(Autores, id=id)
    activo = autor_a_modificar.activo
    autor_a_modificar.activo = not autor_a_modificar.activo
    autor_a_modificar.save()
    
    if activo:
        return HttpResponseRedirect(reverse('app_autores:listar_autores_activos'))
    else:
        return HttpResponseRedirect(reverse('app_autores:listar_autores_inactivos'))
    

class AutoresCreateView(CreateView):
    model = Autores
    fields = "__all__"
    success_url = reverse_lazy("app_autores:listar_autores")
    template_name = "app_frases/crear.html"
    
    
class AutoresUpdateView(UpdateView):
    model = Autores
    fields = "__all__"
    success_url = reverse_lazy("app_autores:listar_autores")
    template_name = "app_frases/crear.html"  
    