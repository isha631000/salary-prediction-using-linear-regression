#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as nm
import pandas as pd
import matplotlib as plt
import tensorflow as tf
from tensorflow import keras
def predict_salary(year):
    x=[0,1,2,3,4,5,6]
    y=[0.5,1.0,1.5,2.0,2.5,3.0,3.5]
    model=keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
    model.compile(optimizer="sgd",loss='mean_squared_error')
    model.fit(x,y,epochs=10)
    return model.predict(year)[0][0]
prediction=predict_salary([9.0])
print("the salary of the person with 9 years of experience should be ")
print(prediction*100,"thousand dollars")


# In[6]:


def predict_salary(year):
    x=[0,1,2,3,4,5,6]
    y=[0.5,1.0,1.5,2.0,2.5,3.0,3.5]
    model=keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
    model.compile(optimizer="sgd",loss='mean_squared_error')
    model.fit(x,y,epochs=200)
    return model.predict(year)[0][0]
prediction=predict_salary([9.0])
print("the salary of the person with 9 years of experience should be ")
print(prediction*100,"thousand dollars")


# In[ ]:




