# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:40:30 2023

@author: chitra
"""

import json

employee = {'name': 'John',
            'age':55,
            'salary':4000.0,
            'isMarried': True,
            'isHavingCar': None}

#json_string = json.dumps(employee,indent=4)
#print(json_string)

with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)
    print("Serialization Done")
 
with open('emp.json','r') as f:
    emp_dict = json.load(f)
    
print(type(emp_dict))

for key, value in emp_dict.items():
    print(key,':',value)
