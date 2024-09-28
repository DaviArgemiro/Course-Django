from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from datetime import date

from agenda.models import Evento

# Create your views here.
def index(request):
    evento = Evento.objects.exclude(
        date__lt = date.today()
    )
    
    return render(request, 'agenda/listar_evento.html', {'evento': evento})

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'agenda/exibir_evento.html', {'evento': evento})

def participar(request):
    evento_id = request.POST.get('evento_id')
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()

    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))