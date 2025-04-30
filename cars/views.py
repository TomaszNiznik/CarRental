from django.shortcuts import render, get_object_or_404
from .models import Car

def index(request):
    return render(request, 'cars/index.html.jinja')

def category_list(request):
    # Przekazujemy listę krotek bez przekształcania w dict
    categories = Car.CAR_CLASSES
    return render(request, 'cars/category.html.jinja', {'categories': categories})

def category(request, category_id=None):
    if category_id:
        # Filtrujemy samochody po kategorii
        cars_in_category = Car.objects.filter(category=category_id)
        category_name = dict(Car.CAR_CLASSES).get(category_id)  # Pobieramy nazwę kategorii
        return render(request, 'cars/category.html.jinja', {
            'cars': cars_in_category,
            'category_id': category_id,
            'category_name': category_name  # Przekazujemy nazwę kategorii
        })
    
    # Jeśli nie ma category_id, wyświetlamy listę kategorii (opcjonalne, fallback)
    categories = Car.CAR_CLASSES
    return render(request, 'cars/category.html.jinja', {'categories': categories})

def car(request, car_id):
    # Szczegóły konkretnego samochodu
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car.html.jinja', {'car': car})

def rent(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/rent.html.jinja', {'car': car})
