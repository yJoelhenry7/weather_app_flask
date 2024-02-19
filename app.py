# app.py
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        weather = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon']
        }
        return weather
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather = get_weather(city)
    if weather:
        return render_template('weather.html', weather=weather)
    else:
        return render_template('error.html', message='City not found')

if __name__ == '__main__':
    app.run(debug=True)
