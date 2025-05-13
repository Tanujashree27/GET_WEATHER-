
````markdown
# Weather Webhook for Dialogflow 🌦️

This project is a simple webhook service built using Flask that integrates Dialogflow with the OpenWeatherMap API to provide real-time weather updates for a given city.

## Features

- Receives POST requests from Dialogflow
- Extracts the city name from user input
- Fetches current weather data using OpenWeatherMap API
- Sends back temperature and weather description as a response

## Requirements

- Python 3.x
- Flask
- Requests
- OpenWeatherMap API key
- Dialogflow agent setup

## Installation

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/weather-webhook.git
cd weather-webhook
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set your API key:**

Edit `webhook.py` and replace the placeholder with your [OpenWeatherMap API](https://openweathermap.org/api) key:

```python
WEATHER_API_KEY = "your_api_key_here"
```

4. **Run the Flask app:**

```bash
python webhook.py
```

The app will start on `http://localhost:5000`.

## Dialogflow Configuration

1. In your Dialogflow agent, go to **Fulfillment** and enable **Webhook**.
2. Set the URL to your deployed server endpoint:

   ```
   https://<your-domain-or-ngrok-url>/webhook
   ```
3. In the **Intent**, enable **Webhook call for this intent**.
4. Add a training phrase like:

   ```
   What’s the weather in New York?
   ```
5. Ensure the entity `geo-city` is used to extract the city name.

## Sample Response

If the user says:

```
What's the weather in Delhi?
```

The response will be:

```
The weather in Delhi is 30°C with clear sky.
```


