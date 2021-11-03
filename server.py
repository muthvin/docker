from flask import Flask, request, jsonify
import json
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

#Load the model
model = pickle.load(open('model.pkl','rb'))
labels ={
  0: "versicolor",   
  1: "setosa",
  2: "virginica"
}

