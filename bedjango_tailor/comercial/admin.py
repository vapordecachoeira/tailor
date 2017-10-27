from django.contrib import admin

from .models import Contrato, Empresa, Contato, EstagioNegociacao


class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 0


class ContatoInline(admin.TabularInline):
    model = Contato
    exclude = (
        'uuid', 'slug', 'date_joined', 'country', 'preferred_language', 'is_staff', 'is_active', 'is_superuser',
        'last_login', 'groups', 'user_permissions', 'password', 'username')
    extra = 0


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'contratos_abertos', 'vagas', 'cidade')
    inlines = [
        ContatoInline,
        ContratoInline,
    ]


class ContratoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'estagio', 'vagas', 'valor')


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'first_name', 'last_name', 'email', 'telefone', 'celular')
    exclude = (
        'uuid', 'slug', 'date_joined', 'country', 'preferred_language', 'is_staff', 'is_active', 'is_superuser',
        'last_login', 'groups', 'user_permissions', 'password', 'username')


admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(EstagioNegociacao)
admin.site.register(Empresa, EmpresaAdmin)
