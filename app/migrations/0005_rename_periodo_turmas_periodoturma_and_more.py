# Generated by Django 5.0.3 on 2024-04-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_area_nome_alter_cursos_carga_horaria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turmas',
            old_name='periodo',
            new_name='periodoturma',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='periodo',
            field=models.CharField(verbose_name='Período do curso'),
        ),
    ]
