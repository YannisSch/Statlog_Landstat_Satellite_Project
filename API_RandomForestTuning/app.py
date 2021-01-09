import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import pandas as pd
app = Flask(__name__)

#-------------- Modele --------
filename = "finalized_model_for_middle_pixel.pkl"
modele=joblib.load(filename)

########

#-------------- Fonction ------------------
def nb_predict(nb):
    tab = ["terre rouge","la culture du coton","sol gris","sol gris humide","sol avec chaumes de vegetation","classe de mélange (tous les types présents)","sol gris tres humide"]
    return tab[nb-1]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    print("Loading Prediction")

    print(request.form)
    print(type(request))

    pixel_int = [int(x) for x in request.form.values()]
    print(pixel_int)

    pixel_values = {
            "r1": pixel_int[0],
            "r2": pixel_int[1],
            "r3": pixel_int[2],
            "r4":pixel_int[3]
        }

    pixel_values = pd.DataFrame(pixel_values, index=[0])

    predict = modele.predict(pixel_values)
    output = predict[0]
    classe = nb_predict(output)

    stat_pred = modele.predict_proba(pixel_values)
    stat_max =(np.max(stat_pred))*100
    stat_max = round(stat_max,2)
    return render_template('index.html', prediction_text=f'Le pixel correspond à {classe} (classe {output}) avec un probabilité de {stat_max} %')

@app.route('/predict_api',methods=['POST'])
def ppp():
    print(request.form)
    return "Ok"


if __name__ == "__main__":
    app.run(debug=True)