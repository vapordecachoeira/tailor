from django.db import models

from base.choices import ChoicesMeta
from comercial.models import Empresa
from tailor.models import Pessoa


class Vaga(models.Model):

    class Status(metaclass=ChoicesMeta):

        EM_NEGOCIACAO_CLIENTE = 'Em negociação com cliente'
        ATIVA = 'Ativa'
        INATIVA = 'Inativa'
        PARALISADA = 'Paralisada'
        FECHADA = 'Fechada'

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    documento = models.FileField('Documento Original', upload_to='vaga_documentos/%Y/%m/%d/', null=True, blank=True)

    status = models.CharField('Status da Vaga', max_length=128, default=Status.ATIVA, choices=Status)

    funcionario_responsavel = models.ForeignKey(
        'users.User',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name='Funcionário Responsável pela vaga'
    )

    def candidatos(self):
        return Aplicacao.objects.filter(vaga=self).count()

    def __str__(self):
        return self.titulo + ' na ' + str(self.empresa)

    class Meta:

        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'


class EtapaRecrutamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:

        verbose_name = 'Etapa de Recrutamento'
        verbose_name_plural = 'Etapas de Recrutamento'


class Candidato(Pessoa):
    nome_sem_acento = models.TextField(null=True, blank=True)
    endereco = models.TextField('Endereço', null=True, blank=True)
    escolaridade = models.TextField('Escolaridade', null=True, blank=True)
    experiencia = models.TextField('Experiência', null=True, blank=True)
    area_interesse = models.TextField('Área(s) de interesse', null=True, blank=True)
    idade = models.IntegerField('Idade', default=0, blank=True, null=True)
    linkedin = models.URLField(max_length=1024, blank=True)
    github = models.URLField(max_length=1024, blank=True)

    cv = models.FileField('Curriculum Vitae', upload_to='candidato_cv/%Y/%m/%d/', null=True, blank=True)

    anexo1 = models.FileField('Anexo 1 (Arquivo)', upload_to='candidato_anexo/%Y/%m/%d/_1/', null=True, blank=True)
    anexo2 = models.FileField('Anexo 2 (Arquivo)', upload_to='candidato_anexo/%Y/%m/%d/_2/', null=True, blank=True)
    anexo3 = models.FileField('Anexo 3 (Arquivo)', upload_to='candidato_anexo/%Y/%m/%d/_3/', null=True, blank=True)
    anexo4 = models.FileField('Anexo 4 (Arquivo)', upload_to='candidato_anexo/%Y/%m/%d/_4/', null=True, blank=True)
    anexo5 = models.FileField('Anexo 5 (Arquivo)', upload_to='candidato_anexo/%Y/%m/%d/_5/', null=True, blank=True)

    obs = models.TextField('Observações', null=True, blank=True)

    pretensao_salarial = models.DecimalField('Pretensão Salarial', max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:

        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

    def aplicacoes(self):
        return Aplicacao.objects.filter(candidato=self).count()


class Aplicacao(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    etapa = models.ForeignKey(EtapaRecrutamento, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

    funcionario_conduzindo = models.ForeignKey(
        'users.User',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name='Funcionário conduzindo aplicação'
    )

    class Meta:

        verbose_name = 'Aplicação'
        verbose_name_plural = 'Aplicações'
        unique_together = [['vaga', 'candidato']]
