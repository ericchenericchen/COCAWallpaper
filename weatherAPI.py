import requests
import json

# OpenWeatherMap API: https://openweathermap.org/current
OWM_API_KEY = 'e8463a344affe52b5803a9be423491e0' #MY API KEY DON'T SPAM OVER 1000 PLEASE :)

#Oslo Norway
DEFAULT_LAT = 59.9139
DEFAULT_LON = 10.7522

#Next step do command line arguments for latitude and longitude so that we can customize the location
#better.

def get_weather(lat, lon):
    params = {
        'appid': OWM_API_KEY,
        'lat': lat,
        'lon': lon, 
        'units': 'imperial'
    }

    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params)

    if response.status_code == 200: # Status: OK
        data = response.json()

        # # PRINTS THE WHOLE JSON, UNCOMMENT IF YOU WANT TO FIND OTHER INFO
        # print(json.dumps(data, sort_keys=True, indent=4))

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        location = data["name"]
        weather = data["weather"][0]["description"]
        gust = data["wind"]["gust"]

        return (temperature, humidity, location, weather, gust)

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return 0.0, 0.0, "N/A", "N/A", 0.0

def weather_init(lat=DEFAULT_LAT, lon=DEFAULT_LON):
    # Working parameters
    # temperature, humidity, location, general weather, wind speed
    temp, hum, city, weather, gust = get_weather(lat, lon)
    
    output = f'{temp}F, {hum}% humidity, {gust}mph gust'
    print(f'weather for {city}: {output}')
    print(f'description: {weather}')

    return output

if __name__ == '__main__':
    weather_init()