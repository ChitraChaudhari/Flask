# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:27:46 2023

@author: chitra
"""

import pickle

class Employee:
    def __init__(self, eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
        
    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'
              .format(self.eno,self.ename,self.esal,self.eaddr))
        
emp = Employee(101, 'John', 4500, 'NYC')

with open('emp.pkl','wb') as f:
    pickle.dump(emp,f)
    print("Pickling Completed")
    
with open('emp.pkl', 'rb') as f:
    obj = pickle.load(f)
    print("Unpickling Completed")
    obj.display()