from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, create_model
import joblib
import pandas as pd
import json
import os

app = FastAPI(title="Credit Risk Prediction API")

# Load model artifacts
MODEL_PATH = 'models/model.joblib'
COLUMNS_PATH = 'models/columns.joblib'
METADATA_PATH = 'models/metadata.json'

if not all(os.path.exists(p) for p in [MODEL_PATH, COLUMNS_PATH, METADATA_PATH]):
    raise RuntimeError("Model artifacts not found. Please run train_model.py first.")

model = joblib.load(MODEL_PATH)
trained_columns = joblib.load(COLUMNS_PATH)
with open(METADATA_PATH, 'r') as f:
    feature_metadata = json.load(f)

# Define dynamic input model based on metadata
input_fields = {}
for name, meta in feature_metadata.items():
    if meta['type'] == 'numerical':
        input_fields[name] = (float, ...)
    else:
        input_fields[name] = (str, ...)

CreditApplication = create_model('CreditApplication', **input_fields)

@app.get("/api/features")
async def get_features():
    return feature_metadata

@app.post("/api/predict")
async def predict(data: CreditApplication):
    try:
        # Convert input to DataFrame
        input_dict = data.dict()
        input_df = pd.DataFrame([input_dict])

        # Preprocess: One-hot encoding
        # Identify categorical columns from metadata
        cat_cols = [name for name, meta in feature_metadata.items() if meta['type'] == 'categorical']
        
        # Apply get_dummies to the input
        input_encoded = pd.get_dummies(input_df, columns=cat_cols)
        
        # Reindex to match trained columns, filling missing with 0
        input_final = input_encoded.reindex(columns=trained_columns, fill_value=0)

        # Predict
        prediction = model.predict(input_final)[0]
        probability = model.predict_proba(input_final)[0].tolist()

        risk_category = "Bad" if prediction == 1 else "Good"
        confidence = probability[1] if prediction == 1 else probability[0]

        return {
            "prediction": int(prediction),
            "risk_category": risk_category,
            "confidence": round(confidence, 4),
            "probabilities": probability
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Serve static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
