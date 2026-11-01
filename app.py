import json
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

try:
    model = joblib.load("student_result_model.pkl")
except Exception:
    model = None

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    required_fields = ["attendance", "internal_marks", "assignment_marks", "previous_score"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    input_df = pd.DataFrame([data])
    pred = model.predict(input_df)[0]
    result = "PASS" if pred == 1 else "FAIL"

    return jsonify({
        "prediction": result,
        "prediction_code": int(pred)
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
