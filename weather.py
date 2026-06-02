import requests
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        current = data["current_condition"][0]
        print("\n===== Weather Report =====")
        print("City:", city)
        print("Temperature:", current["temp_C"], "°C")
        print("Feels Like:", current["FeelsLikeC"], "°C")
        print("Condition:", current["weatherDesc"][0]["value"])
        print("Humidity:", current["humidity"], "%")
        print("Wind Speed:", current["windspeedKmph"], "km/h")
        print("==========================")
    except Exception as e:
        print("Error:", e)
while True:
    city = input("\nEnter city name (or quit): ")
    if city.lower() == "quit":
        print("Program Closed")
        break
    get_weather(city)