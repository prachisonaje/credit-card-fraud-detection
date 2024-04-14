from flask import Flask, make_response, request, jsonify, send_file
from joblib import dump, load
import pandas as pd
import pathlib

app = Flask(__name__)

counter_file = "counter.joblib"

pathlib.Path("data").mkdir(parents=True, exist_ok=True)
if not pathlib.Path(counter_file).exists():
    dump(0, counter_file)

# models
LogisticRressionCV = load("LogisticRressionCV.joblib")
AdaBoost = load("AdaBoost.joblib")
XGBoost = load("XGBoost.joblib")
Random_Forest = load("Random_Forest.joblib")
Isolation_Forest = load("Isolation_Forest.joblib")
#Local_Outlier_Factor = load("Local_Outlier_Factor.joblib")
Support_Vector_Machine = load("Support_Vector_Machine.joblib")
DecisionTreeClassifier = load("DecisionTreeClassifier.joblib")

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files["file"]
    # TODO: check if file is csv
    counter = load(counter_file)
    uploaded_file.save(f"data/{counter}.csv")
    dump(counter + 1, counter_file)

    request_data = request.form.to_dict()
    file_data = {
        "id": counter,
        "filename": request_data["filename"] or f"file_{counter}.csv",
        "description": request_data["description"] or "No description provided",
    }

    dump(file_data, f"data/{counter}.joblib")

    return make_response(jsonify({"id": counter}), 200)

@app.get("/files")
def return_list_of_files():
    files = []
    for file in pathlib.Path("data").iterdir():
        if file.is_file() and file.suffix == ".csv":
            files.append(load(f"data/{file.stem}.joblib"))
    return make_response(jsonify(files), 200)


@app.get("/data/<int:file_id>")
def return_file(file_id):
    return send_file(f"data/{file_id}.csv")

@app.get("/predictions/<int:file_id>")
def report(file_id):    
    file_data = load(f"data/{file_id}.joblib")

    #return precalculated
    if "predictions" in file_data:
        return make_response(jsonify(file_data["predictions"]), 200)
    
    #calculate
    df = pd.read_csv(f"data/{file_id}.csv")
    predictions = {
        "AdaBoost": list(map(int,AdaBoost.predict(df))),
        "DecisionTreeClassifier": list(map(int,DecisionTreeClassifier.predict(df))),
        #"Local_Outlier_Factor": list(map(int,Local_Outlier_Factor.predict(df))),
        "LogisticRressionCV": list(map(int,LogisticRressionCV.predict(df))),
        "Random_Forest": list(map(int,Random_Forest.predict(df))),
        #"Support_Vector_Machine": list(map(int,Support_Vector_Machine.predict(df))),
        #"Isolation_Forest": list(map(int,Isolation_Forest.predict(df))),
        "XGBoost": list(map(int,XGBoost.predict(df))),
    }
    
    file_data["predictions"] = predictions
    dump(file_data, f"data/{file_id}.joblib")

    return make_response(jsonify(predictions), 200)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)


