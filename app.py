from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# carregar modelo de diabetes
with open("model/modelo_diabetes.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "API de Diabetes funcionando!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # pegar lista de features
    features = np.array(data["features"]).reshape(1, -1)

    prediction = model.predict(features)

    return jsonify({
        "prediction": int(prediction[0]),
        "resultado": "Diabetes" if prediction[0] == 1 else "Sem Diabetes"
    })

if __name__ == "__main__":
    app.run(debug=True)