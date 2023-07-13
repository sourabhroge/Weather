# create a virtual environment and install all the modules
# import flask module
from flask import Flask,render_template,request
import requests

app = Flask(__name__)

# make a route and render html template to this route
@app.route('/', methods =['GET','POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']

        # Make a request to the API using the provided city name and API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=d21506e9b5b698452de142a20600628b'
        response = requests.get(url)
        weather_data = response.json()

        # Extract relevant weather information
        temp = weather_data['main']['temp']   # this temperature is in kelvin
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        temperature = str(temp-273.15)   # this converts kelvin to centigrade

        # Render the template with the weather data
        return render_template('weather.html', city=city, temperature=temperature, humidity=humidity, wind_speed=wind_speed)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)