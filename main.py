from flask import Flask, render_template, request
import numpy as np
import joblib
import os


app = Flask(__name__)


@app.route('/')
def home():
    return <h1>my first web app</h1>


    
   # run application
if __name__ == "__main__":
    app.run(debug=True)    
