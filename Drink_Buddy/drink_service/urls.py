from django.urls import path
from . import views

urlpatterns = [
    path('drinks/', views.drinks, name= 'drinks'),
    path("recipe_detail/<int:id>/", views.recipe_detail, name='drink_service-detail'),
    path('search/',views.search_drinks, name= 'search_drinks' ),
    
    
]