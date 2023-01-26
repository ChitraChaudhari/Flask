# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:34:09 2023

@author: chitra
"""

from flask import Flask, jsonify, request, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl",'rb'))
 
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    pred_price = model.predict(features)
    return render_template("index.html",prediction_text = "The Chances of Admissions are :  {}".format(pred_price))

#driver function
if __name__ == '__main__':
    app.run(debug=True)
    