from django.shortcuts import render, redirect
from .models import Drinks, UserLocation, Drink
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import requests
from decouple import config
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages


def home(request):
    Drink = Drinks.objects.all()
    return render(request, 'drink_service/home.html', {'Drink': Drink})
        
@login_required
def logoutuser(request):
    if request.method == 'POST': #make it quick
        logout(request)
        return redirect('home')

def landing_page(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        UserLocation.objects.create(location=location)
        return redirect('response_page')
    return render(request, 'drink_service/landing_page.html')

def response_page(request):
    user_location = UserLocation.objects.latest('id')
    location = user_location.location

    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
    response = requests.get(url)

    try:
        #response.status_code==200
        # Make API call to retrieve weather information
         
        weather_data = get_weather_data(location)

        # Extract required weather data
        temperature = weather_data['current']['temp_c']
        description = weather_data['current']['condition']['text']
        time_data = weather_data['location']['localtime']
        icon_weather = weather_data['current']['condition']['icon']
        icon_link = 'https://' + icon_weather

        # Make API call to retrieve local time information
        local_time = time_data.split()[1]  # Extract time from datetime string

        # Extract local hour
        local_hour = int(local_time.split(':')[0])
        #local_hour = int(local_time[:1])
        
        # Extract required weather data
        temperature = weather_data['current']['temp_c']
    
        # Get matching recipes from the database
        recipes = get_matching_recipes(temperature, local_hour)

    except:
        return render(request, 'drink_service/home.html',{'error': 'Invalid Location name'})
      
    context = {
        'location': location,
        'temperature': temperature,
        'description': description,
        'local_time': local_time, 
        'local_hour': local_hour,
        #'icon': icon_weather,
        'recipes': recipes,
        'icon_link': icon_link
    }
    
    return render(request, 'drink_service/response_page.html', context)

  
def get_weather_data(location):
    # Make an API call to retrieve weather information based on the location
    # Replace 'API_KEY' with your actual API key
    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
    response = requests.get(url)
    if response.status_code==200:
        weather_data = response.json()
    return weather_data

def get_local_time_data(location):
    # Make an API call to retrieve local time information based on the location
    # Replace 'API_KEY' with your actual API key
    api_key = 'API_KEY'
    url = f'https://worldtimeapi.org/api/timezone/{location}'
    response = requests.get(url)
    time_data = response.json()
    return time_data


def get_matching_recipes(temperature, local_hour):
    # Get matching recipes from the database based on temperature and local time ranges
    if local_hour >= 5 and local_hour <= 11:
        time_range = "5 to 11"
    elif local_hour >= 12 and local_hour <= 23:
        time_range = "12 to 23"
    else:
        return []

    if temperature >= -15 and temperature < 0:
        temperature_range = "-15 to 0"
    elif temperature >= 0 and temperature < 10:
        temperature_range = "0 to 10"
    elif temperature >= 10 and temperature < 20:
        temperature_range = "10 to 20"
    else:
        temperature_range = "20+"

 # Get matching recipes based on time and temperature ranges
    recipes = Drink.objects.filter(timeofday=time_range, temperatureoflocation=temperature_range)[:3]
    return recipes


def premium(request):
    return render(request, 'drink_service/premium.html')


def recipe_detail(request, id):
    recipe = Drink.objects.get(id=id)
    return render(request, 'drink_service/recipe_detail.html', context={"recipe": recipe})


# def drinks(request):
#     context = {
#         'recipes': Drink.objects.all() 
#     }
#     return render(request, 'drink_service/drinks.html', context)


def drinks(request):
    recipes = Drink.objects.all()
    paginator = Paginator(recipes, 10)  # Show 10 pictures per page

    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)

    return render(request, 'drink_service/drinks.html', {'recipes': recipes})


def search_drinks(request):
    if request.method == 'GET':
        # Get the search parameters from the request
        name = request.GET.get('name')
        ingredients = request.GET.get('ingredients')
        temperature = request.GET.get('temperature')
        time_of_day = request.GET.get('time_of_day')
        time_of_year = request.GET.get('time_of_year')
        social_situation = request.GET.get('social_situation')
        mood = request.GET.get('mood')
        # Filter the drinks based on the search parameters
        recipes = Drink.objects.all()
        if name:
            recipes = recipes.filter(name__icontains=name)
        if ingredients:
            recipes = recipes.filter(ingredients__icontains=ingredients)
        if temperature:
            recipes = recipes.filter(temperatureoflocation=temperature)
        if time_of_day:
            recipes = recipes.filter(timeofday=time_of_day)
        if time_of_year:
            recipes = recipes.filter(timeofyear__icontains=time_of_year)
        if social_situation:
            recipes = recipes.filter(socialsituation__icontains=social_situation)
        if mood:
            recipes = recipes.filter(mood__icontains=mood)
        paginator = Paginator(recipes, 10)  # Show 10 pictures per page

        page_number = request.GET.get('page')
        recipes = paginator.get_page(page_number)
        return render(request, 'drink_service/search.html', {'recipes': recipes})
        
    return render(request, 'drink_service/search.html', {'recipes': recipes})

