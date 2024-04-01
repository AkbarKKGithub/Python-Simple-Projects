import requests

def get_weather(city):
    api_key = 'f7da5b6b47d5213a006bec438d62fa91'  # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data


city = input("Enter city name: ")
weather_data = get_weather(city)
if weather_data['cod'] == 200:  # Check if the response status code is OK
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    print(f"Weather in {city}: {description}, Temperature: {temperature}°C")
else:
    print("City not found or error in fetching weather data.")


