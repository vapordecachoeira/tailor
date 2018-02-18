from django.contrib import admin

from recrutamento.models import Vaga
from .models import Contrato, Empresa, Contato, EtapaNegociacao


class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 0


class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 0
    fields = ('nome', 'email', 'telefone', 'celular')


class VagaInline(admin.TabularInline):
    model = Vaga
    extra = 0


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'contratos_abertos', 'vagas', 'cidade')
    list_filter = ('cidade', )
    search_fields = ('nome', )
    inlines = [
        ContatoInline,
        ContratoInline,
        VagaInline
    ]


class ContratoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'etapa', 'vagas', 'valor')
    list_filter = ('etapa', 'empresa')
    search_fields = ('empresa__nome',)


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'nome', 'email', 'telefone', 'celular')
    list_filter = ('empresa',)
    search_fields = ('empresa__nome', 'nome', 'email')


admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(EtapaNegociacao)
admin.site.register(Empresa, EmpresaAdmin)
