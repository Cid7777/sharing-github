from keys import api_key
import requests
import csv

city = 'Kyoto'
country = 'JP'
units = "metric"
lang = "ja"

res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units={units}&lang={lang}")
data = res.json()
#print(data['wind']['speed'])

weather = data['weather'][0]['main']
temp = data['main']['temp']
wind = data['wind']['speed']

header = ['city', 'country_code', 'weather', 'temp', 'wind_speed']
info = [city, country, weather, temp, wind]

with open('weather.csv', 'w') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerow(info)


