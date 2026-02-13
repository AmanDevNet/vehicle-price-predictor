
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

MODEL_PATH = "model.pkl"

# Load model on startup
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        logger.info("Model loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
else:
    logger.warning("Model file not found. Please train the model first.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        data = request.json
        logger.info(f"Received prediction request: {data}")
        
        # Create DataFrame from input
        input_data = pd.DataFrame([data])
        
        # Predict
        prediction = model.predict(input_data)[0]
        logger.info(f"Prediction: {prediction}")
        
        return jsonify({'prediction': round(prediction, 2)})
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
