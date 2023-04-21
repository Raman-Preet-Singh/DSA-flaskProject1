# app.py
import json

import pymongo as PyMongo
from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
uri = "mongodb+srv://RootUser:Raman1234@cluster0.sfqudim.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["CurrenData"]
column = db["Cur"]
x = column.find_one()
print(x)
key_pair = next(iter(x))
print(key_pair)
x[key_pair] = 'Curreny Value Analysis'
key_value = x.pop('IDR')
key_value = x.pop('KRW')
print(x)

@app.route('/')
def google_pie_chart():
    return render_template('index.html')

@app.route("/google_pie_chart_barchat/barchat")
def google_pie_chart_barchat():
    return render_template('barchat.html',data=x)

@app.route('/google_pie_chart_normal/piechart')
def google_pie_chart_normal():
    return render_template('piechart.html',data=x)
@app.route('/google_pie_chart_donuchat/2D-chart')
def google_pie_chart_donuchat():
    return render_template('donuchat.html', data=x)

if __name__ == "__main__":
    app.run()