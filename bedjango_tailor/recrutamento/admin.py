from django.contrib import admin

from .models import Candidato, Candidatura, EstagioRecrutamento, Vaga


class CandidaturaInline(admin.TabularInline):
    model = Candidatura
    extra = 0


class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'telefone', 'candidaturas')
    exclude = (
        'uuid', 'slug', 'date_joined', 'country', 'preferred_language', 'is_staff', 'is_active', 'is_superuser',
        'last_login', 'groups', 'user_permissions', 'password', 'username')
    inlines = [
        CandidaturaInline,
    ]

class VagaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'titulo', 'candidatos')

class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('vaga', 'estagio', 'candidato')


admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Candidatura, CandidaturaAdmin)
admin.site.register(EstagioRecrutamento)
admin.site.register(Vaga, VagaAdmin)
