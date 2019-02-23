import json
import requests
response = requests.get("http://ipinfo.io/json")
jsonData = json.loads(response.text)
city = jsonData["city"]

api_key = "979701f1a7473a05462c4a1296994c42"

base_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

#add the variables to the url
complete_url = base_url.format(city,api_key)

weather_data = requests.get(complete_url).json()
location = weather_data["name"]
sys = weather_data["sys"]
country = sys["country"]
main = weather_data["main"]
temp = main["temp"]
tempp = temp-273.15
tempertature = '%.0f' % tempp
basic_final = "The weather in {},{} is {} degrees"
final = basic_final.format(location,country,tempertature)


#creat a txt file and write the result
file = open("weather.txt","w")
file.write(final)
file.close()

print()

cities = ['london', 'tel+aviv', 'jerusalem', 'rome', 'barcelona', 'ashdod', 'prague', 'madrid', 'budapest', 'haifa']
for i in cities:
    final_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    complete_final_url = final_url.format(i,api_key)
    weather_final = requests.get(complete_final_url).json()
    location2 = weather_final["name"]
    sys2 = weather_final["sys"]
    country2 = sys2["country"]
    main2 = weather_final["main"]
    temp2 = main2["temp"]
    tempp2 = temp2 - 273.15
    tempertature2 = '%.0f' % tempp2
    basic_final2 = "The weather in {},{} is {} degrees"
    final2 = basic_final2.format(location2, country2, tempertature2)
    print (final2)
