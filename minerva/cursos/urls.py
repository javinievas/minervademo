from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "cursos"

urlpatterns = [
    path('', views.home, name="home"),
    path('cursos/', views.cursos, name="list"),
    path('cursos/nuevo/', views.curso_nuevo, name="nuevo"),
    path('cursos/<int:id>/', views.curso_detail, name="detail"),
    path('cursos/<int:id>/editar/', views.curso_editar, name="editar"),
    path('cursos/<int:id>/borrar/', views.curso_borrar, name="borrar"),
    path('cursos/<int:id>/alumnos/nuevo/', views.curso_nuevo_alumno, name="nuevo_alumno"),
    path('cursos/<int:id>/alumnos/<int:alumno_id>/editar/', views.curso_editar_alumno, name="editar_alumno"),
    path('cursos/<int:id>/alumnos/<int:alumno_id>/borrar/', views.curso_borrar_alumno, name="borrar_alumno"),
]
