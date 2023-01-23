# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 09:11:53 2023

@author: chitra
"""
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

USAhousing = pd.read_csv('USA_Housing.csv')

X= USAhousing[['Avg. Area Income', 'Avg. Area House Age','Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y= USAhousing['Price']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)

pickle.dump(lm,open('model.pickle','wb'))
