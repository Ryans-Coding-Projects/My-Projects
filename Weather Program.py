import requests
import json

api_key = "YOUR_API_KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter the name of the city: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

data = response.json()

if data["cod"] != "404":
    print("Current temperature: " +
          str(data["main"]["temp"]) +
          "\nAtmospheric pressure: "+
          str(data["main"]["pressure"]) +
          "\nHumidity: " +
          str(date["main"]["humidity"]) +
          "\nMinimum Temperature: " +
          str(data["main"]["temp_min"]) +
          "\nMaximum Temperature: " +
          str(data["main"]["temp_max"]))

else:
    print("City not found ")
