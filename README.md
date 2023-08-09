# Drink_Buddy
# PROJECT NAME: Drink_Buddy
The aim of this project is to develop a user-friendly web application, Drink Buddy, that revolutionizes the way people discover and enjoy beverages. By leveraging weather conditions, moods, and personal preferences, Drink Buddy suggests the perfect drink for every occasion. Whether it's a hot summer day, a cozy rainy afternoon, or a need for an energizing boost, users can rely on Drink Buddy to recommend a tailored beverage experience. With an intuitive interface, real-time data, and a vast database of drink options, the app aims to enhance users' beverage choices, introduce them to new flavors, and ultimately elevate their overall drinking satisfaction.

## Description
The Drink Buddy App helps you discover the perfect drink for any occasion by combining real-time weather data with a curated collection of drink recipes. It takes into account your location, temperature, and time of day to suggest beverages that suit your preferences and the current weather conditions.

## Key Features:
Landing Page: Enter your location information to get started.
Weather Integration: Retrieve the local weather conditions using APIs.
Time-Based Recommendations: Recommend drinks based on the time of day.
Temperature-Driven Suggestions: Suggest beverages based on the temperature at your location.
Rich Recipe Collection: Access a diverse range of drink recipes.
Personalized Experience: Receive tailored recommendations based on your location and preferences.
Responsive Design: Enjoy a seamless experience on both desktop and mobile devices.
Whether you're planning a party, looking to try something new, or simply want to enjoy a drink that complements the weather outside, Drink Buddy App is your go-to companion.

## Technologies Used
Python
Django
Django Rest Framework
PostgreSQL
HTML
CSS
APIs for weather and time data (e.g., OpenWeatherMap, WorldTimeAPI)

## Installation
Clone the repository:
git clone https://github.com/AriMichel/Drink_Buddy

### Install the project dependencies:
pip install -r requirements.txt

### Set up the database:
Create a PostgreSQL database.

### Update the database configuration in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_host',
        'PORT': 'your_port',
    }
}

### Set up the environment variables:
Create a .env file in the project root directory.
Add the required environment variables:
WEATHER_API_KEY=your_weather_api_key
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=your_port

#### Migrate the database:
python manage.py migrate

### Run the development server:
python manage.py runserver

### Access the application:
Open a web browser and navigate to http://localhost:8000.

## Usage
On the landing page, enter your location information (e.g., city name, postal code) and submit the form.
The application will retrieve the local weather and time information using APIs.
On the response page, you will see the following information:
Location: [Location information]
Temperature: [Temperature in Celsius]
Weather Description: [Weather condition]
Local Time: [Local time]
Recommended Recipes: [List of recommended drink recipes]

## License
The Drink Buddy App is released under the MIT license.

## Contributing
We welcome contributions from the community! If you'd like to contribute to the Drink Buddy App, please refer to our contribution guidelines in the README file.

## Contact
For any inquiries or support related to the Drink Buddy App, please reach out to our team at worlddrinkbuddy@gmail.com.

## Basic Features:
- Easy access
- Fun and User- Friendly Interface
- Weather and location based recommendations
- Strong data base with lots of drink recipes and information
- Marketing strategies
- Account creation to access premium content
- A search Option for premium accounts

## Advanced Features & Outlook:
Social Integration: Users can connect their social media accounts to share favorite drink recommendations, experiences, and photos. This promotes engagement, discussions about drinks, and allows users to discover new beverages based on friends' recommendations.
Personalized Notifications: Intelligent notifications remind users of favorite drinks, suggest new beverages based on preferences and past selections, and notify about limited-time offers or discounts at preferred coffee shops. This
Augmented Reality (AR) Experience: Users can virtually visualize their chosen drink in real-world environments using their smartphone's camera. This interactive experience helps them make informed decisions and enhances engagement.
Gamification Elements: Badges, achievements, and challenges tied to beverage exploration reward users for trying new drinks, visiting different coffee shops, and participating in quizzes or competitions. This adds a fun element and encourages exploration.
Integration with Smart Home Devices: Users can control smart home devices like coffee machines through the app. They can brew their recommended drink or adjust coffee settings, providing a convenient and seamless beverage experience at home.
Integration with other apps/services.

## OUTLOOK
As Drink Buddy grows in popularity, expand features and collaborate with local coffee shops for exclusive discounts. Implement ratings and reviews to aid informed choices. With updates, engagement, and partnerships, Drink Buddy can become a go-to app for beverage enthusiasts, offering a personalized discovery platform.