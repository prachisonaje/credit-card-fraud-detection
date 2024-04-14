from flask import Flask, make_response, request, jsonify
from joblib import dump, load
import pandas as pd
import pathlib

app = Flask(__name__)

counter_file = 'data/counter.joblib'

pathlib.Path('data').mkdir(parents=True, exist_ok=True)
if not pathlib.Path(counter_file).exists():
    dump(0, counter_file)

model1=load('LogisticRressionCV.joblib')

@app.route('/upload', methods=['POST'])
def upload():
    request_data = request.form.to_dict()
    uploaded_file = request.files['file']

    counter = load(counter_file)
    uploaded_file.save(f'data/{counter}.csv')
    dump(counter + 1, counter_file)

    return make_response(jsonify({'id': counter}), 200)

@app.route('/reports', methods=['POST'])
def report():
    counter = request.json['id']
    df = pd.read_csv(f'data/{counter}.csv')
    df = df.drop(['Class'], axis=1)
    prediction = model1.predict(df)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)