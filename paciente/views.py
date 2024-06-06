from django.shortcuts import render
from medico.models import DadosMedico, Especialidades, DatasAbertas
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(resquest):
    if resquest.method == "GET":
        medico_filtrar = resquest.GET.get('medico')
        especialidades_filtrar = resquest.GET.getlist('especialidades')
        medicos = DadosMedico.objects.all()

        if medico_filtrar:
            medicos = medicos.filter(nome__icontains=medico_filtrar)
        
        if especialidades_filtrar:
            medicos = medicos.filter(especialidade_id__in=especialidades_filtrar)
        especialidades = Especialidades.objects.all()
        return render(resquest, 'home.html', {'medicos': medicos, 'especialidades': especialidades})


def escolher_horario(request, id_dados_medicos):
    if request.method == 'GET':
        medico = DadosMedico.objects.get(id=id_dados_medicos)
        dastas_abertas = DatasAbertas.objects.filter(user=medico.user).filter(data__gte=datetime.now()).filter(agendado=False)

        return render(request, 'escolher_horario.html', {'medico': medico, 'datas_abertas': dastas_abertas,})