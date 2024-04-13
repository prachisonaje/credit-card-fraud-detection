from flask import Flask, make_response, request, jsonify
import joblib
import pandas as pd
import pathlib

app = Flask(__name__)


model1=joblib.load('LogisticRressionCV.joblib')

@app.route('/upload', methods=['POST'])
def upload():
    request_data = request.get_data()
    uploaded_file = request.files['file']
    df = pd.read_csv(uploaded_file)
    df = df.drop(['Class'], axis=1)
    prediction = model1.predict(df)
    print(prediction)
    print(request_data)
    return make_response(jsonify([10,11,12]), 200)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)