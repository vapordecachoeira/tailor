from django.contrib import admin

from .models import Candidato, Aplicacao, EtapaRecrutamento, Vaga


class AplicacaoInline(admin.TabularInline):
    model = Aplicacao
    extra = 0


class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'aplicacoes', 'area_interesse')
    search_fields = ('nome__unaccent', 'email')
    ordering = ('nome', 'email', 'area_interesse')
    inlines = [
        AplicacaoInline,
    ]


class VagaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'titulo', 'candidatos', 'status')
    list_filter = ('empresa', 'empresa__cidade', 'status')
    search_fields = ('empresa__nome', 'titulo')
    ordering = ('titulo', 'empresa', 'status')

    inlines = [
        AplicacaoInline, # TODO separar por estágio
    ]


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


class AplicacaoAdmin(admin.ModelAdmin):
    list_display = ('vaga', 'etapa', 'candidato')
    list_filter = (('etapa__nome', custom_titled_filter('Etapa')), 'vaga__empresa__cidade')

    search_fields = ('candidato__nome', 'vaga__titulo', 'vaga__empresa__nome')

    ordering = ('vaga', 'etapa', 'candidato')


admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Aplicacao, AplicacaoAdmin)
admin.site.register(EtapaRecrutamento)
# TODO ver os candidos nesse estágio
admin.site.register(Vaga, VagaAdmin)
