from padelpy import from_smiles

from tensorflow import keras
import pickle
import numpy as np

# calculate molecular descriptors for propane
descriptors = from_smiles('CCC')
E_model = keras.models.load_model('E_model.h5', compile=False)
S_model = keras.models.load_model('S_model.h5', compile=False)
A_model = keras.models.load_model('A_model.h5', compile=False)
B_model = keras.models.load_model('B_model.h5', compile=False)
Scaler = pickle.load(open("Scaler.pkl",'rb'))
feature_name = list(pickle.load(open("feature_name.pkl",'rb')))



#print(descriptors["McGowan_Volume","apol"])
#print(len(descriptors))
feature_name = list(pickle.load(open("feature_name.pkl",'rb')))
used = map(lambda x: descriptors[x],feature_name)
Scaler = pickle.load(open("Scaler.pkl",'rb'))
features= Scaler.transform(np.array(list(used)).reshape(1,-1))
result = {"E": E_model.predict(features), "S": S_model.predict(features),
          "A": A_model.predict(features), "B": B_model.predict(features),
          "V": descriptors["McGowan_Volume"]}
print(result)


