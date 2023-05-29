import requests

API_KEY = '6634e18b2e360b650265045ae49562d1'

data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY}").json()

for i in data['hourly']:
    for j in i['weather']:
        if j['id'] < 700:
            print("You should probably take an umbrella")


