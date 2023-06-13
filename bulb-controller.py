# This code intents to switch on / off a bulb, attached to a ESP8266 controller, through Thinger

from flask import Flask, render_template, request
import requests

app = Flask(__name__)
httpHeaders = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1Nzk0NTQ5MjMsImlhdCI6MTU3OTQ0NzcyMywidXNyIjoibmFrb3YifQ.ywbCx8ckmm_Bzi0hfVFRJRDNUXjvMLgssfcDtyIvVtc'}

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/switchOn', methods=['POST'])
def switchOn():
    requests.get(
        'https://api.thinger.io/v2/users/nakov/devices/esp8266bulb/bulbSwitchOn',
        headers = httpHeaders
    )
    return render_template("index.html")

@app.route('/switchOff', methods=['POST'])
def switchOff():
    requests.get(
        'https://api.thinger.io/v2/users/nakov/devices/esp8266bulb/bulbSwitchOff',
        headers = httpHeaders
    )
    return render_template("index.html")

app.run()
