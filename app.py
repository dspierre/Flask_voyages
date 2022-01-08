#Run simple API using Flask
#@AvocadoAUN
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import requests
import json
app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    modelfile = 'modele/model_SVM.pkl'
    model=p.load (open(modelfile, 'rb'))
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)




