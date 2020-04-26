from flask import Flask, render_template, request
import requests
import random

from pulsesensor import Pulsesensor
import time

p = Pulsesensor()
p.startAsyncBPM()

app = Flask(__name__)

@app.route('/')
def index():
    print("index !!!!")
    return render_template('index.html')


@app.route('/suggestions')
def suggestions():
    bpm = p.BPM
    #if bpm > 0:
    if bpm > 220 and bpm < 235:
        text = bpm - 170
        print("BPM: %d" % text)
    else:
        #print("No Heartbeat found")
        text = 0
        print("BPM: 0")
    return render_template('suggestions.html', suggestions=text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
    #app.run(debug=True)
