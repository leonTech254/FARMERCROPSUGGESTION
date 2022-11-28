from flask import Flask, request, jsonify
import numpy as np
from fruitsData import fdata
import pickle


app = Flask(__name__)


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)
    loaded_model = pickle.load(open("./SVM.pickle", "rb"))
    result = loaded_model.predict(to_predict)
    return result


@app.route("/team-project/4.1", methods=['POST', 'GET'])
def machine_leaning_data():
    if request.method == "POST":

        contents = request.get_json()
        temp = contents['temp']
        humidity = contents['humidity']
        ph = contents['ph']
        rainfall = contents['rainfall']
        data = []
        data.append(temp)
        data.append(humidity)
        data.append(ph)
        data.append(rainfall)
        result = ValuePredictor(data)
        fdata[result[0]]
        finalREsult = {"predicted": result[0],
                       "predictedMoreInfo": fdata[result[0]]}

        return jsonify({"data": finalREsult})


if __name__ == "__main__":
    app.run(port=5000)
