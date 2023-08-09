from django.test import TestCase, Client
from django.urls import reverse, include
from unittest.mock import patch, MagicMock
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserLocation, Drink
from .views import landing_page, response_page, get_weather_data, get_local_time_data, get_matching_recipes, recipe_detail
from decouple import config

# Create your tests here.

class LandingPageTests(TestCase):
     # Tests that home.html template is rendered
    def test_render_home_template(self):
        response = self.client.get('/')
        assert response.status_code == 200
        assert 'drink_service/home.html' in [template.name for template in response.templates]

    # AI Generated Test:
    def test_landing_page_view(self):
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drink_service/landing_page.html')

    def test_landing_page_post(self):
        location = 'Berlin'
        response = self.client.post(reverse('landing_page'), {'location': location})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('response_page'))
        self.assertEqual(UserLocation.objects.count(), 1)
        self.assertEqual(UserLocation.objects.latest('id').location, location)

class ResponsePageTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('drink_service.views.get_weather_data')
    @patch('drink_service.views.get_local_time_data')
    @patch('drink_service.views.get_matching_recipes')
    def test_response_page_view(self, mock_get_matching_recipes, mock_get_local_time_data, mock_get_weather_data):
        # Test the behavior of the response page view
        location = 'Berlin'
        weather_data = {
            'current': {'temp_c': 20, 'condition': {'text': 'Sunny', 'icon': 'icon_weather'}},
            'location': {'localtime': '2023-06-23 12:00'}
        }
        mock_get_weather_data.return_value = weather_data
        mock_get_local_time_data.return_value = {}
        mock_get_matching_recipes.return_value = []

        UserLocation.objects.create(location=location)
        response = self.client.get(reverse('response_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drink_service/response_page.html')
        self.assertEqual(response.context['location'], location)
        self.assertEqual(response.context['temperature'], weather_data['current']['temp_c'])
        self.assertEqual(response.context['description'], weather_data['current']['condition']['text'])
        time_data = weather_data['location']['localtime']
        local_time = time_data.split()[1] 
        self.assertEqual(response.context['local_time'], local_time)
        self.assertEqual(response.context['local_hour'], 12)
        self.assertEqual(response.context['recipes'], [])

    @patch('drink_service.views.requests.get')
    def test_get_weather_data(self, mock_get):
        # Test the get_weather_data helper function
        location = 'Berlin'
        api_key = config('WEATHER_API_KEY')
        expected_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
        expected_weather_data = {'main': {'temp': 20}, 'weather': [{'description': 'Sunny'}]}
        mock_response = MagicMock()
        mock_response.json.return_value = expected_weather_data
        mock_get.return_value = mock_response

        weather_data = get_weather_data(location)

        mock_get.assert_called_with(expected_url)
        self.assertEqual(weather_data, expected_weather_data)

    def test_get_matching_recipes(self):
        # Test the get_matching_recipes helper function
        temperature = 20    
        local_hour = 11
        expected_recipes = []
        len_expected_recipes = len(expected_recipes)
        recipes = get_matching_recipes(temperature, local_hour)
        len_recipes = len(recipes)
        print (recipes)
        self.assertEqual(len_recipes, len_expected_recipes)


# class LoginTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.username = 'testuser'
#         self.password = 'testpassword'
#         self.user = User.objects.create_user(username=self.username, password=self.password)

#     def test_login_get(self):
#         # Test the behavior of the login view with a GET request
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'drink_service/login.html')

#     def test_login_post_invalid_credentials(self):
#         # Test the behavior of the login view with a POST request and invalid credentials
#         response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrong password'})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'drink_service/login.html')
#         self.assertIn('error', response.context)
#         self.assertEqual(response.context['error'], 'Username and password do not match')

#     def test_login_post_valid_credentials(self):
#         # Test the behavior of the login view with a POST request and valid credentials
#         response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('premium'))
#         self.assertEqual(response.wsgi_request.user.is_authenticated, True)

class RecipeDetailTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.recipe = Drink.objects.create(id = 1, name='Test Recipe', ingredients='Ingredient 1, Ingredient 2', recipe='Step 1, Step 2')

    '''def test_recipe_detail_view(self):
        # Test the behavior of the recipe_detail view
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drink_service/recipe_detail/<int:id>/')

        #path("recipe_detail/<int:id>/", views.recipe_detail, name='drink_service-detail'),
        self.assertEqual(response.context['recipe'], self.recipe)'''
    
class HomeTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        # Test the behavior of the home view
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drink_service/home.html')
        self.assertIn('Drink', response.context)
        
class PremiumTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_premium_view(self):
        # Test the behavior of the premium view
        response = self.client.get(reverse('premium'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drink_service/premium.html')

class DrinksTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_drinks_view(self):
        # Test the behavior of the drinks view
        response = self.client.get(reverse('drinks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drink_service/drinks.html')
        self.assertIn('recipes', response.context)
        # Add more assertions as needed