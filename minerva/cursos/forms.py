from django import forms
from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = []
