from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("List of Cars")


def car (request, car_id):
    return HttpResponse("Description of singke car")

def category (request, category_id):
    return HttpResponse("List of cars from single category")