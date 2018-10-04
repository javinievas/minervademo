from django.db import models


class Modalidad(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='Modalidades'


class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    horas = models.IntegerField(default=10)
    modalidad = models.ForeignKey("Modalidad", on_delete=models.SET_NULL, null=True, blank=True)
    subvencionado = models.BooleanField(default=False)
    plazas = models.PositiveSmallIntegerField(default=25)
    horario = models.CharField(max_length=50, choices=(("m", "Mañana"), ("t", "Tarde")))

    def porcentaje_plazas(self):
        return self.alumnomatriculado_set.all().count() * 100 // self.plazas

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ("fecha_inicio", "-nombre")



class AlumnoMatriculado(models.Model):
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    fecha_matricula = models.DateTimeField(auto_now_add=True)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)
