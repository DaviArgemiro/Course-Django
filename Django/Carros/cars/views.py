from django.shortcuts import render

# Create your views here.
def cars_view(request):
    return render(request, 'cars.html')