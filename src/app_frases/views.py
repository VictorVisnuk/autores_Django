from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Frases
# Create your views here.

class FrasesListView(LoginRequiredMixin, ListView):
    #model = Frases
    queryset = Frases.objects.all()
    template_name = "app_frases/listar.html"    
    context_object_name = "lista_frases"
    

class FrasesVisiblesListView(LoginRequiredMixin, ListView):
    #model = Frases
    queryset = Frases.objects.filter(visible = True)
    template_name = "app_frases/listar.html"    
    context_object_name = "lista_frases"
    

class FrasesInvisiblesListView(LoginRequiredMixin, ListView):
    #model = Frases
    queryset = Frases.objects.filter(visible = False)
    template_name = "app_frases/listar.html"    
    context_object_name = "lista_frases"
    

class FrasesAutorListView(LoginRequiredMixin, ListView):
    model = Frases
    template_name = "app_frases/listar.html"    
    context_object_name = "lista_frases"
    
    def get_queryset(self):
        id_autor = self.kwargs.get('id')
        return Frases.objects.filter(autor=id_autor)


class FrasesCreateView(LoginRequiredMixin, CreateView):
    model = Frases
    fields = "__all__"
    success_url = reverse_lazy("app_frases:listar")
    template_name = "app_frases/crear.html"
    
    
class FrasesUpdateView(LoginRequiredMixin, UpdateView):
    model = Frases
    fields = "__all__"
    success_url = reverse_lazy("app_frases:listar")
    template_name = "app_frases/crear.html"
    

class FrasesDeleteView(LoginRequiredMixin, DeleteView):
    model = Frases
    success_url = reverse_lazy("app_frases:listar")
    template_name = "app_frases/borrar.html"
    

def listar_json(request):
    frases = get_list_or_404(Frases)
    autores_json = serializers.serialize("json", frases)
    return JsonResponse(autores_json, safe=False)       