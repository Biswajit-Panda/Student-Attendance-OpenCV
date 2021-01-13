import numpy as np
from flask import Flask, request, jsonify, render_template
import dataColection

# Create the Flask app
app = Flask(__name__)

# Load the pkl file

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Collect Data
@app.route('/collect', methods=['POST'])
def collect():
    return render_template('collect.html')

# Train Model
@app.route('/model_training', methods=['POST'])
def model_training():
    return render_template('collect.html', prediction_text='Model Trained...')

# Prediction Function
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    # output = round(prediction[0],2)
    print(int_features)
    dataColection.collectCapture(int(int_features[0]),int_features[1])

    return render_template('collect.html', prediction_text='success...')

if __name__ == "__main__":
    app.run(debug=True)
