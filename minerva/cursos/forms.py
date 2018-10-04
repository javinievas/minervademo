from django import forms
from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = []


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = AlumnoMatriculado
        exclude = ["curso", ]
