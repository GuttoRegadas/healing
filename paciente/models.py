from django.db import models
from django.contrib.auth.models import User
from medico.models import DatasAbertas
from django.contrib.auth.models import User

# Create your models here.


class Consulta(models.Model):
    status_shoices = (
        ('A', 'Agendado'),
        ('F', 'Finalizada'),
        ('C', 'Cancelada'),
        ('I', 'Iniciada'),
    )
    paciente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_aberta = models.ForeignKey(DatasAbertas, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_shoices, default='A')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.paciente.username