from django.contrib import admin

from .models import *


class ModalidadAdmin(admin.ModelAdmin):
    search_fields = ["nombre", ]

admin.site.register(Modalidad, ModalidadAdmin)


class AlumnoMatriculadoInline(admin.TabularInline):
    model = AlumnoMatriculado


class CursoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "plazas", "fecha_inicio", "fecha_fin", "horas", "modalidad", "subvencionado"]
    list_filter = ["subvencionado", "modalidad"]
    search_fields = ["nombre", ]
    inlines = [
        AlumnoMatriculadoInline,
    ]

admin.site.register(Curso, CursoAdmin)
