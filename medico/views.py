from django.shortcuts import render, redirect
from .models import Especialidades, DadosMedico, is_medico
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

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
            especialidade_id=especialidade,
            descricao=descricao,
            valor_consulta=valor_consulta,
            user=request.user

        )

        dados_medico.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro médigo realizado com sucesso!')
        return redirect('/medicos/abrir_horario')
    
    
    
def abrir_horario(request):

    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente Médicos podem acessar essa página!')
        return redirect('/usuarios/sair')
    
    if request.mothod == "GET":
        return render(request, 'abrir_horario.html')