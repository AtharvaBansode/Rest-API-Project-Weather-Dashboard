from flask import Flask, render_template, request, redirect, url_for
import requests
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if city:
        params = {
            'q': city,
            'appid': app.config['WEATHER_API_KEY'],
            'units': 'metric'
        }
        response = requests.get(app.config['WEATHER_API_URL'], params=params)
        weather_data = response.json()
        return render_template('weather.html', weather=weather_data)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

