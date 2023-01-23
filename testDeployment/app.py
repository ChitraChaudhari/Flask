# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 09:32:18 2023

@author: chitra

Using Flask to make an api

"""
from flask import Flask, jsonify, request, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl",'rb'))
 
@app.route('/')
def home():
    '''
    if(request.method=='GET'):
        data = "Hello World!"
        return jsonify({'data':data})
    '''
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def predict():
    '''
    #odel = pickle.load(open('model.pkl','rb'))
    income = request.args.get('income')
    house_age = request.args.get('house_age')
    rooms = request.args.get('rooms')
    bedrooms = request.args.get('bedrooms')
    population = request.args.get('population')
    
    test_df = pd.DataFrame({'Income':[income], 'House_Age':[house_age], 'Rooms':[rooms],'Bedrooms':[bedrooms],'Population':[population]})
    
    pred_price = model.predict(test_df)
    
    #return jsonify({'House Price':str(pred_price)})
    '''
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    pred_price = model.predict(features)
    return render_template("index.html",prediction_text = "The House Price is {}".format(pred_price))

#driver function
if __name__ == '__main__':
    app.run(debug=True)
    