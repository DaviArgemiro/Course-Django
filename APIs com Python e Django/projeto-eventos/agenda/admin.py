from django.contrib import admin
from agenda.models import Evento, Categoria

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'local', 'link')
    search_fields = ('nome',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Categoria, CategoriaAdmin)