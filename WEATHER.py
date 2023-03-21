import requests #lets you import data from api
import json #temp weather humidity another parameter
api_key = "f70e260a636bad384a68cb089c0c0549"
city = input("city:")
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key)
response = requests.get(url)
data = response.json()
print(data)
weather=data['weather'][0]['description']
print("The current weather condition is "+ weather)
temp_in_kelvin= data['main']['temp']
temp_in_celcius= temp_in_kelvin - 273.15
print("The current temperature is "+ str(temp_in_celcius) +"C"+ " or " +str(temp_in_kelvin)+"K")
pressure= data['main']['pressure']
print("Today's pressure is "+ str(pressure)+"Pa")
humidity=data['main']['humidity']
print("The humidity is "+str(humidity)+"%")
wind_speed= data['wind']['speed']
print( "The windspeed is " +str(wind_speed)+" mph")


