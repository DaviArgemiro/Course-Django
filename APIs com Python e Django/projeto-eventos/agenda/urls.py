from django.urls import path
from agenda.views import index, exibir_evento, participar

urlpatterns = [
    path("", index, name='listar_eventos_raiz'),
    path("eventos/", index, name='index'),
    path("evento/<int:id>", exibir_evento, name='exibir_evento'),
    path("participar/", participar, name="participar"),
]