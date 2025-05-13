from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
WEATHER_API_KEY = "your_openweathermap_api_key"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    
    # Extract city name from Dialogflow request
    city = req.get("queryResult").get("parameters").get("geo-city")

    if city:
        weather = get_weather(city)
        response_text = f"The weather in {city} is {weather}."
    else:
        response_text = "I couldn't find the weather. Please try again."

    return jsonify({"fulfillmentText": response_text})

def get_weather(city):
    """Fetches weather details from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        return f"{temp}°C with {weather_desc}"
    else:
        return "not available"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
