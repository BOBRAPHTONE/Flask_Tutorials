#!/bin/python

#getting weather of major cities around the world using OpenWeather API

import requests
import json

#API key from OpenWeather map
api_key = "26c7d541b9d4a453df49d961bf746589"

#base url from OpenWeathermap
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Please enter your favourite city :")

complete_url = base_url + "appid=" +api_key + "&q" +city

#use requests to get the data 

response = requests.get(complete_url)
#print(response)
data = response.json() # converting the response into json data format

print(data['main'])








