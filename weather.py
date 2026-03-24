import requests

def weather():
    api_key = "28405a7444b2ecca9ae50ec91e966c79" 
    city = "Colombo"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return "Weather not found"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"{temp}°C {desc}"

result = weather()
print(result)