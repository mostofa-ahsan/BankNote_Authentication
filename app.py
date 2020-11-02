# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:38:27 2020

@author: mosto
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)
pickle_in = open('classifier_rf.pkl','rb')
classifier = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"





if __name__ == '__main__':
    app.run()