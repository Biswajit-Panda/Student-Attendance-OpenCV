import numpy as np
from flask import Flask, request, jsonify, render_template
import dataColection
import modelTraining

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

# Attendance 
@app.route('/attendance', methods=['POST'])
def attendance():
    return render_template('take_attendance.html')

# Attendance Sheet
@app.route('/attendance_sheet', methods=['POST'])
def attendance_sheet():
    return render_template('attendance_sheet.html')

# Train Model
@app.route('/model_training', methods=['POST'])
def model_training():
    modelTraining.train_model()
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
