import requests

# Replace 'Your_API_Key' with your actual WeatherAPI.com API key
api_key = "d390ccd096654f43a41205730241701"

def get_weather(city):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}

    response = requests.get(base_url, params=params)
    data = response.json()

    if "error" in data:
        print(f"Error: {data['error']['message']}")
    else:
        location = data["location"]["name"]
        temperature_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather in {location}:")
        print(f"Temperature: {temperature_c}°C")
        print(f"Condition: {condition}")

if __name__ == "__main__":
    user_city = input("Enter the name of the city: ")
    get_weather(user_city)
