from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *


def home(request):
    proximos = Curso.objects.all().order_by("-fecha_inicio")[:3]
    return render(request, "cursos/home.html", {
            "proximos": proximos,
        })

def cursos(request):
    qs = Curso.objects.all()
    modalidades = Modalidad.objects.all()
    modalidad_filtrada = request.GET.get("modalidad", None)

    if modalidad_filtrada:
        qs = qs.filter(modalidad__id=modalidad_filtrada)
    return render(request, "cursos/list.html", {
        "cursos": qs,
        "modalidades": modalidades,
        })


def curso_nuevo(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.add_message(request, messages.INFO, 'Curso creado correctamente')
            return redirect("cursos:detail", id=obj.id)
    else:
        form = CursoForm()

    return render(request, "cursos/nuevo.html", {"form": form,  "title":"Nuevo curso"})


def curso_detail(request, id):
    obj = get_object_or_404(Curso, id=id)

    return render(request, "cursos/detail.html", {
        "curso": obj,
        })

def curso_editar(request, id):
    obj = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            messages.add_message(request, messages.INFO, 'Curso actualizado correctamente')
            return redirect("cursos:detail", id=obj.id)
    else:
        form = CursoForm(instance=obj)

    return render(request, "cursos/nuevo.html", {"form": form, "title":"Editar curso"})


def curso_borrar(request, id):
    obj = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        try:
            obj.delete()
        except:
            messages.add_message(request, messages.ERROR, 'Ha ocurrido un error inesperado al borrar')
            return redirect("cursos:list")
        messages.add_message(request, messages.INFO, 'Curso borrado correctamente')
        return redirect("cursos:list")

    return render(request, "cursos/borrar.html", {"curso": obj})


def curso_nuevo_alumno(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.curso = curso
            obj.save()
            messages.add_message(request, messages.INFO, 'Alumno creado correctamente')
            return redirect("cursos:detail", id=curso.id)
    else:
        form = AlumnoForm()

    return render(request, "cursos/nuevo_alumno.html", {"form": form,  "title":"Nuevo alumno"})


def curso_editar_alumno(request, id, alumno_id):
    pass

def curso_borrar_alumno(request, id, alumno_id):
    pass
