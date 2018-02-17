from django.contrib import admin

from .models import Candidato, Aplicacao, EtapaRecrutamento, Vaga


class AplicacaoInline(admin.TabularInline):
    model = Aplicacao
    extra = 0


class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'telefone', 'candidaturas')
    exclude = (
        'uuid', 'slug', 'date_joined', 'country', 'preferred_language', 'is_staff', 'is_active', 'is_superuser',
        'last_login', 'groups', 'user_permissions', 'password', 'username')
    inlines = [
        AplicacaoInline,
    ]


class VagaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'titulo', 'candidatos')

    inlines = [
        AplicacaoInline,
    ]


class AplicacaoAdmin(admin.ModelAdmin):
    list_display = ('vaga', 'etapa', 'candidato')


admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Aplicacao, AplicacaoAdmin)
admin.site.register(EtapaRecrutamento)
admin.site.register(Vaga, VagaAdmin)
