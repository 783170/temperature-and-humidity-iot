import requests, json

def getweather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key=ee0c7eee0f92434db0a203120250605&q={city}&days=1&aqi=no&alerts=no"

    response = requests.get(url)

    x = response.json()

    print("Current temperature in St. Paul from weather API:", x["current"]["temp_c"], " C")
    print("Current temperature in St. Paul from weather API:", x["current"]["temp_f"], " F")
    print("Current humidity in St. Paul from weather API:", x["current"]["humidity"])