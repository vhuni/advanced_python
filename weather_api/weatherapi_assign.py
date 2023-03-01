import requests

class Weatherapp:
    city = None
    humudity = None
    temp = None
    description = None

    def __init__(self):
        self.city_name = input('Enter a city: ')
        if self.city_name == '':
            assert False, 'Please enter a city'
        elif self.city_name.strip().isdigit():
            assert False, 'Please enter a valid city name'
        else:
            Weatherapp.city = self.city_name
        self.get_weather()

    def get_weather(self):
        self.city = Weatherapp.city
        ## self.api_key = 'secret_api key'
        self.url = 'https://api.openweathermap.org/data/2.5/weather?q=' + f'{self.city}' + '&appid='+ f'{self.api_key}'
        self.response = requests.get(self.url)
        self.weather = self.response.json()
        if self.weather['cod'] == '404':
            assert False, 'City not found in weather database'
        Weatherapp.description = self.weather 
        self.get_weather_description()

    def get_weather_description(self):
        self.weather_desc = Weatherapp.description
        print(type(self.weather_desc))
        print(f'{Weatherapp.city.title()}\'s Weather: ', self.weather_desc['weather'][0]['description'])
        print(f'{Weatherapp.city.title()}\'s Humidity: ', self.weather_desc['main']['humidity'])
        print(f'{Weatherapp.city.title()}\'s Temperature: ', self.weather_desc['main']['temp'], 'Fahrenheit')

if __name__ == '__main__':
    Weatherapp()
