# Generated by Django 5.0.3 on 2024-04-08 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_disciplinasporcursos_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinasporcursos',
            name='disciplinasporcursos',
            field=models.CharField(max_length=100, verbose_name='Disciplina por Curso'),
        ),
        migrations.AlterField(
            model_name='disciplinasporcursos',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.periodo', verbose_name='Período'),
        ),
    ]