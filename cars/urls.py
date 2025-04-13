from django.urls import path
from . import views

# Dodaj app_name
app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),  # Strona główna
    path('category/', views.category_list, name='category_list'),  # Lista kategorii
    path('category/<str:category_id>/', views.category, name='category'),  # Szczegóły danej kategorii
    path('<int:car_id>/', views.car, name='car'),  # Szczegóły samochodu
    path('rent/<int:car_id>/', views.rent, name='rent'),  # Wynajem samochodu
]



