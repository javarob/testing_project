import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import psycopg2
from config import password

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# conn = psycopg2.connect(host="localhost", database="tbm",
#                         user="postgres", password="Issimo86*")


# engine = create_engine('postgresql://postgres:' +
#                        password + '@localhost:5432/tbm')
# data = engine.execute("SELECT * FROM stock_data")

# for x in data:
#     print(x)

# connection=engine.connect()

# engine = create_engine("postgresql://postgres:" +
#                        password + "@localhost:5432/Homework09")
# connection = engine.connect()


##################################################


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/stockdata')
def stockdata():
    engine = create_engine('postgresql://postgres:' +
                           password + '@localhost:5432/tbm')

    data = engine.execute(
        "SELECT id, adj_open, adj_close, symbol, end_val, date_str FROM stock_data")
    newdata = []

    for x in data:
        d = {
            'id': x[0],
            'adj_open': x[1],
            'adj_close': x[2],
            'symbol': x[3],
            'end_val': x[4],
            'date_str': x[5]
        }
        newdata.append(d)

    return jsonify(newdata)


@app.route('/years')
def getyears():
    engine = create_engine('postgresql://postgres:' +
                           password + '@localhost:5432/tbm')

    data = engine.execute(
        "select distinct date_part('year',date) as date from stock_data order by date;")
    newdata = []

    for x in data:
        d = {
            'year': x[0]
        }
        newdata.append(d)

    return jsonify(newdata)


if __name__ == "__main__":
    app.run(debug=True)
