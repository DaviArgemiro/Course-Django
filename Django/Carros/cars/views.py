from django.http import HttpResponse

# Create your views here.
def cars_view(request):
    return HttpResponse('Meus carros')