# Weather data app

import requests
from pprint import pp, pprint

API_Key = 'a2a46c3bc8cef9e38bea15a95b6faeb5'

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
