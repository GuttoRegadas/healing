# Generated by Django 5.0.4 on 2024-04-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_teste_rename_medico_dadosmedico_especialidades_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialidades',
            name='teste',
        ),
        migrations.DeleteModel(
            name='Teste',
        ),
    ]
