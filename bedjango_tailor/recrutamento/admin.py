from django.contrib import admin

from .models import Candidato, Aplicacao, EtapaRecrutamento, Vaga


class AplicacaoInline(admin.TabularInline):
    model = Aplicacao
    extra = 0


class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'aplicacoes')
    search_fields = ('nome', 'email')
    inlines = [
        AplicacaoInline,
    ]


class VagaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'titulo', 'candidatos')
    list_filter = ('empresa', 'empresa__cidade')
    search_fields = ('empresa__nome', 'titulo')

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


admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Aplicacao, AplicacaoAdmin)
admin.site.register(EtapaRecrutamento)
# TODO ver os candidos nesse estágio
admin.site.register(Vaga, VagaAdmin)
