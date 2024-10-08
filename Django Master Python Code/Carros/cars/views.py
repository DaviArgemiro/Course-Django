from django.shortcuts import render
from cars.models import Car
from cars.forms import CarModelForm
from django.shortcuts import redirect

# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('brand__name')
    search = request.GET.get('search')

    if(search):
        cars = Car.objects.filter(model__contains=search)
    

    return render(
            request,
            'cars.html', 
            {'cars': cars}
        )

def new_car_view(request):
    if(request.method == 'POST'):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if(new_car_form.is_valid()):
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    
    return render(request, 'new_car.html', {'new_car_form': new_car_form})