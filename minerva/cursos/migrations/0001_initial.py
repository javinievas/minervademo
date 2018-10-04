# Generated by Django 2.1.2 on 2018-10-01 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('horas', models.IntegerField(default=10)),
                ('subvencionado', models.BooleanField(default=False)),
                ('plazas', models.PositiveSmallIntegerField(default=25)),
                ('turno', models.CharField(choices=[('m', 'Mañana'), ('t', 'Tarde')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='modalidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cursos.Modalidad'),
        ),
    ]
