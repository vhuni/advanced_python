import requests


def get_weather(city):
    api_key = 'eaeab850760a6f2d218ddb5decd21c40'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + f'{city}' + '&appid='+ f'{api_key}'
    print(url)
    response = requests.get(url)
    weather = response.json()

    return print(weather)

if __name__ == '__main__':
    input = input('Enter a city: ')
    if input == '':
        assert False, 'Please enter a city'
    elif input.strip().isdigit():
        assert False, 'Please enter a city name'
    else:
        city = input

    get_weather(city)
