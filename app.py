import numpy as np
from tensorflow import keras
from flask import Flask, request, jsonify, render_template
import pubchempy as pcp
import pickle
from keras import backend
from padelpy import from_smiles

app = Flask(__name__)

#model = pickle.load(open('model.pkl','rb'))
E_model = keras.models.load_model('E_model.h5', compile=False)
S_model = keras.models.load_model('S_model.h5', compile=False)
A_model = keras.models.load_model('A_model.h5', compile=False)
B_model = keras.models.load_model('B_model.h5', compile=False)
Scaler = pickle.load(open("Scaler.pkl",'rb'))
feature_name = list(pickle.load(open("feature_name.pkl",'rb')))
#print(feature_name)
@app.route('/')
def home():
    return render_template('page3.html')

@app.route('/predict', methods=['POST'])
def submit():
    features_list = [str(x) for x in request.form.values()]
    descriptors = from_smiles(features_list[0])
    features = map(lambda x: descriptors[x], feature_name)
    features = Scaler.transform(np.array(list(features)).reshape(1, -1))
    E = round(float(E_model.predict(features)),2)
    S = round(float(S_model.predict(features)),2)
    A = round(float(A_model.predict(features)),2)
    B = round(float(B_model.predict(features)),2)
    V = round(float(descriptors["McGowan_Volume"]),2)
    Chem = pcp.get_compounds(features_list[0], 'smiles')
    Inform = pcp.compounds_to_frame(Chem, properties=['xlogp'])
    logP =  abs(0.562*E-1.054*S+0.034*A-3.46*B+ 3.814*V+0.088- Inform["xlogp"].values)
    goodness = "G" if logP<=0.5 else ("F" if logP<=1 else "B")
    labels = ["SMILES","E","S","A","B","V","Goodness"]
    values = [[features_list[0],E, S, A, B, V, goodness],]
    return render_template('page3.html',labels=labels,values=values)

if __name__ == "__main__":
    app.run(port=80,debug = True)