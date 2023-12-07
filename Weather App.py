import requests
api_key = "96cc1b19b38f5507dee101dddfdb0676"

city = input("Enter the City Name: ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'


response = requests.get(url)
print('***********************************')

if response.status_code == 200:
    data = response.json()
    # print(data)
    temp = data['main']['temp']
    humidity=data['main']['humidity']
    pressure=data['main']['pressure']
    desc = data['weather'][0]['description']
    sunrise=data['sys']['sunrise']
    sunset=data['sys']['sunset']    
    country=data['sys']['country']
    visibility=data['visibility']
    city = data["name"]

    print(f'City: {city}')
    print(f'Country: {country}')
    print(f'Temperature: {temp-273.15:.3f} C')
    print(f'Description: {desc}')
    print(f'Sunrise: {sunrise}')
    print(f'Sunset: {sunset}')
    print(f'Visibility: {visibility}')
    print(f'Humidity: {humidity} %')
    print(f'Pressure: {pressure} hPa')
else:
    print('Error fetching weather data')
print('***********************************')
