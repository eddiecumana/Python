# Weather data app

import requests
from pprint import pp, pprint

API_Key = ''

city = input("\nEnter a city: ")
country = input("Enter a country: ")
country = country.casefold()

zipcode = ''
commachar = ''


if country == "us":
    commachar = '","'
    zipcode = input("Enter a zipcode: ")

if zipcode == '':
    commachar = ''
    zipcode = ''

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city+","+country+commachar+zipcode

weather_data = requests.get(base_url).json()

pprint(weather_data)
print()
