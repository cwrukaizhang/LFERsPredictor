import numpy as np
from tensorflow import keras
from flask import Flask, request, jsonify, render_template
import pubchempy as pcp
import pickle
from keras import backend
from padelpy import from_smiles

app = Flask(__name__)
models = [keras.models.load_model(ele+'_model.h5', compile=False) for ele in ['E',"S","A","B"]]
Scaler = pickle.load(open("Scaler.pkl",'rb'))
feature_name = list(pickle.load(open("feature_name.pkl",'rb')))
@app.route('/')
def home():
    return render_template('page.html')

@app.route('/predict', methods=['POST'])
def submit():
    features_list = [str(x) for x in request.form.values()]
    descriptors = from_smiles(features_list[0])
    features = map(lambda x: descriptors[x], feature_name)
    features = Scaler.transform(np.array(list(features)).reshape(1, -1))
    prediction = [round(float(model.predict(features)),2) for model in models]
    V = round(float(descriptors["McGowan_Volume"]),2)
    Inform = pcp.compounds_to_frame(pcp.get_compounds(features_list[0],'smiles'), properties=['xlogp','synonyms'])
    cids = pcp.get_cids(features_list[0], 'smiles')
    Surrogates =  abs(0.562*prediction[0]-1.054*prediction[1]+0.034*prediction[2]-
                      3.46*prediction[3]+ 3.814*V+0.088- Inform["xlogp"].values)
    goodness = "G" if Surrogates<=0.5 else ("F" if Surrogates<=1 else "B")
    labels = ["Name","SMILES","CID","E","S","A","B","V","Goodness"]
    values = [[list(Inform['synonyms'])[0][0].title()]+[features_list[0]]+cids+prediction+[V]+[goodness],]
    return render_template('page.html',labels=labels,values=values)

if __name__ == "__main__":
    app.run(port=80,debug = True)