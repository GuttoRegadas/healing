from django.shortcuts import render
from medico.models import DadosMedico

# Create your views here.
def home(resquest):
    if resquest.method == "GET":
        medicos = DadosMedico.objects.all()
        return render(resquest, 'home.html', {'medicos': medicos})