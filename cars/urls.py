from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('car/<car_id>',views.car,name='car'),
    path('category/<category_id>/', views.category, name='category')
]