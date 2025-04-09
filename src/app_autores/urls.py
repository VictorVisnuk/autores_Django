from django.urls import path
from . import views

app_name = "app_autores"

urlpatterns = [
    path('inicial/', views.inicial, name='inicial'),
    path('presentacion/', views.presentacion, name='presentacion'),
    path("listar_json/", views.listar_json, name="listar_json"),   
    path("listar_activos/", views.listar_autores_activos, name="listar_autores_activos"),
    path("listar_inactivos/", views.listar_autores_inactivos, name="listar_autores_inactivos"),
    path("detalle/<int:id>", views.detalle, name="detalle"),
    path("borrar_autor/<int:id>", views.borrar_autor, name="borrar_autor"),
    path("modificar_activo/<int:id>", views.modificar_activo, name="modificar_activo"),
]
