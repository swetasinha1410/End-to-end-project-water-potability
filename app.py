from flask import Flask, render_template, request
import numpy as np
import joblib
import os


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods =['GET','POST'])
def prediction():
    if  request.method=='POST':
    # request all the input fields
        ph = float(request.form['ph value'])
        Hardness = float(request.form['Hardness'])
        Solids = float(request.form['Solids'])
        Chloramines = float(request.form['Chloramines'])
        Sulfate = float(request.form['Sulfate'])
        Conductivity = float(request.form['Conductivity'])
        Organic_carbon = float(request.form['Organic carbon'])
        Trihalomethanes = float(request.form['Trihalomethanes'])
        Turbidity = float(request.form['Turbidity'])

        # create numpy array for all the inputs
        val = np.array([ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity])
        
        #define save model and scaler path
        model_path=os.path.join('model','water_classification_v1.0.model')
        sacler_path=os.path.join('models','water_classification_v1.0.scaler')
        
        
        #Load the model and scaler
        model= joblib.load(open("water_classification_v1.0.model","rb"))
        sacler=joblib.load(open("water_classification_v1.0.scaler","rb"))
        
        
        #transform the input data using pre fitted standard scaler
        data=sacler.transform([val])
        
        #make the prediction 
        prediction=model.predict(data)
        
    
        
        if prediction == 1:
            outcome ='Potable'
        else:
            outcome ='Not Potable'
        return render_template('index.html',prediction_text=outcome)
    return render_template('index.html')

    
    
   # run application
if __name__ == "__main__":
    app.run(debug=True)    

   