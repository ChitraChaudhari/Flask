# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 22:11:25 2023

@author: chitra
"""
from pyaml import yaml

employee = {'name': 'John',
            'age':55,
            'salary':4000.0,
            'isMarried': True,
            'isHavingCar': None}

#Serialization to yaml file
with open('emp.yaml','w') as f:
    yaml.dump(employee, f)
    print("serialization done")
    
#Deserialization from yaml file
with open('emp.yaml','r') as f:
    emp_dict = yaml.safe_load(f)
    
print(emp_dict)