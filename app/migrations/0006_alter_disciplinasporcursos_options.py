# Generated by Django 5.0.3 on 2024-04-08 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_periodo_turmas_periodoturma_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplinasporcursos',
            options={'verbose_name': 'Disciplina por curso', 'verbose_name_plural': 'Disciplinas por curso'},
        ),
    ]
