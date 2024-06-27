from django.shortcuts import render, redirect
from .models import Especialidades, DadosMedico, is_medico, DatasAbertas
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, timedelta
from paciente.models import Consulta

# Create your views here.

def cadastro_medico(request):
    dm = DadosMedico.objects.filter(user=request.user).exists
    if is_medico(request.user):
        messages.add_message(request, constants.WARNING, "Médico já cadastrado" )
        return redirect('/medicos/abriri_horario')
    
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        return render(request, 'cadastro_medico.html', {'especialidades': especialidades})
    elif request.method == "POST":
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')

        #e = Especialidades.objects.filter(especialidade=especialidade).first()

        dados_medico = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            rg=rg,
            cedula_indentidade_medica=cim,
            foto=foto,  
            user=request.user,
            descricao=descricao,
            especialidade_id=especialidade,
            valor_consulta=valor_consulta,

        )

        dados_medico.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro médigo realizado com sucesso!')
        return redirect('/medicos/abrir_horario')
    
    
    
def abrir_horario(request):

    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente Médicos podem acessar essa página!')
        return redirect('/usuarios/sair')
    
    if request.method == "GET":
        dados_medicos = DadosMedico.objects.get(user=request.user)
        datas_abertas = DatasAbertas.objects.filter(user=request.user)
        return render(request, 'abrir_horario.html', {'dados_medicos': dados_medicos, 'datas_abertas': datas_abertas})
    elif request.method == "POST":
        data = request.POST.get('data')

        data_foratada = datetime.strptime(data, '%Y-%m-%dT%H:%M')

        if data_foratada <= datetime.now():
            messages.add_message(request, constants.WARNING, 'A data não pode ser anterior a data atual')
            return redirect('/medicos/abrir_horario')
        
        horario_abrir = DatasAbertas(
            data=data,
            user=request.user,
        )

        horario_abrir.save()

        messages.add_message(request, constants.SUCCESS, 'Horario cadastrado com sucesso.')
        return redirect('/medicos/abrir_horario')
    

'''def consultas_medico(request):
    if not is_medico(request.user):
        print("entrou no if")
        messages.add_message(request, constants.WARNING, 'Somente Médicos podem acessar essa página!')
        return redirect('/usuarios/sair')
    
    hoje = datetime.now().date()

    consultas_hoje = Consulta.objects.filter(data_aberta__user=request.user).filter(data_aberta__data__gte=hoje).filter(data_aberta__data__lt=hoje + timedelta(days=1) )
    consultas_restantes =  Consulta.objects.exclude(id__in=consultas_hoje.values('id'))
    return render(request, 'consultas_medico.html', {"consultas_hoje": consultas_hoje, "consultas_restantes": consultas_restantes})'''

def consultas_medico(request):
    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')
    
    hoje = datetime.now().date()

    consultas_hoje = Consulta.objects.filter(data_aberta__user=request.user)
    print(consultas_hoje)
    consultas_restantes = Consulta.objects.exclude(id__in=consultas_hoje.values('id'))

    return render(request, 'consultas_medico.html', {'consultas_hoje': consultas_hoje, 'consultas_restantes': consultas_restantes, 'is_medico': is_medico(request.user)})