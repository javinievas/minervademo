from django.contrib import admin
from django.urls import path, include, re_path

from . import views

app_name = "cursos"

urlpatterns = [
    path('', views.cursos, name="list"),
    path('nuevo/', views.curso_nuevo, name="nuevo"),
    path('<int:id>/', views.curso_detail, name="detail"),
    path('<int:id>/editar/', views.curso_editar, name="editar"),
    path('<int:id>/borrar/', views.curso_borrar, name="borrar"),
    path('<int:id>/alumnos/nuevo/', views.curso_nuevo_alumno, name="nuevo_alumno"),
    path('<int:id>/alumnos/<int:alumno_id>/editar/', views.curso_editar_alumno, name="editar_alumno"),
    path('<int:id>/alumnos/<int:alumno_id>/borrar/', views.curso_borrar_alumno, name="borrar_alumno"),
]
