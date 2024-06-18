from django import template
from medico.models import DadosMedico, Especialidades, DatasAbertas
from datetime import datetime
import calendar

register = template.Library()

@register.filter(name='teste')
def teste(mes):

    return f'{mes}'