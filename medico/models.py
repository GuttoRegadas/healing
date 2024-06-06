from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def is_medico(user):
    return DadosMedico.objects.filter(user=user).exists()

class Especialidades(models.Model):
    especialidade = models.CharField(max_length=100, verbose_name="Especialidades")
    icone = models.ImageField(upload_to="icones", null=True, blank=True)

    def __str__(self):
        return f'{self.especialidade}'
    

class DadosMedico(models.Model):
    crm = models.CharField(max_length=50, verbose_name='CRM')
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cep = models.CharField(max_length=10, verbose_name="CEP")
    rua = models.CharField(max_length=150, verbose_name="Rua")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    numero = models.IntegerField(verbose_name="Número")
    rg = models.ImageField(upload_to= "rgs",verbose_name="RG")
    cedula_indentidade_medica = models.ImageField(upload_to="cim")
    foto = models.ImageField(upload_to="foto_perfil")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING, null=True, blank=True)
    valor_consulta = models.FloatField(default=100)

    def __str__(self) -> str:
        return f'{self.user.username}'
    
    @property
    def proxima_data(self):
        proxima_data = DatasAbertas.objects.filter(user=self.user).filter(data__gt=datetime.now()).filter(agendado=False).order_by('data').first()
        '''if proxima_data == None:
            return "Nenhuma data agendada."
        else:'''
        return proxima_data
    

class DatasAbertas(models.Model):
    data = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    agendado = models.BooleanField(default=False)

    def __str__(self):
        return {self.user}