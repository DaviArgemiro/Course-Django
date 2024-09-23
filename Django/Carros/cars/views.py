from django.shortcuts import render
from cars.models import Car

# Create your views here.
def cars_view(request):
    cars = Car.objects.filter(brand__name='Fiat')

    return render(
            request,
            'cars.html', 
            {'cars': cars}
        )