from django.urls import path
from . import views
from.views import (
    FrasesListView,
    FrasesVisiblesListView,
    FrasesInvisiblesListView,
    FrasesAutorListView,
    FrasesCreateView,
    FrasesUpdateView,
    FrasesDeleteView,
)

app_name = "app_Frases"

urlpatterns = [
    path("", FrasesListView.as_view(), name="listar"),
    path("listar_visibles", FrasesVisiblesListView.as_view(), name="listar_visibles"),
    path("listar_invisibles", FrasesInvisiblesListView.as_view(), name="listar_invisibles"),
    path("listar_autor/<int:id>", FrasesAutorListView.as_view(), name="listar_autor"),
    path("listar_json/", views.listar_json, name="listar_json"),
    path("crear/", FrasesCreateView.as_view(), name="crear"),
    path("modificar/<int:pk>", FrasesUpdateView.as_view(), name="modificar"),
    path("borrar/<int:pk>", FrasesDeleteView.as_view(), name="borrar"),
]
