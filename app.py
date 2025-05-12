from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    city = request.args.get('city', 'New York')  
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": "your_real_api_key_here", 
        "q": city,
        "aqi": "no"
    }

    weather_data = {}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "location": data["location"]["name"],
            "temp_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"]
        }
    else:
        weather_data = {"error": "Unable to fetch weather data."}

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)