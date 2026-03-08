from fastapi import FastAPI
from pydantic import BaseModel
import logging
import joblib
import json
import numpy as np
from scipy.sparse import hstack, csr_matrix
from feature_pipeline import extract_structured_features

ARTIFACT_DIR = "artifacts"

model = joblib.load(f"{ARTIFACT_DIR}/severity_model.pkl")
vectorizer = joblib.load(f"{ARTIFACT_DIR}/tfidf_vectorizer.pkl")

with open(f"{ARTIFACT_DIR}/metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

THRESHOLD = metadata["threshold"]

logging.basicConfig(
    filename="prediction_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="Public Health Early Warning API", version="1.0")

class PredictionRequest(BaseModel):
    report: str

@app.get("/")
def root():
    return {"message": "Public Health Early Warning System API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(request: PredictionRequest):
    report = request.report

    text_features = vectorizer.transform([report])
    structured = np.array([extract_structured_features(report)])
    structured_sparse = csr_matrix(structured)
    features = hstack([text_features, structured_sparse])

    probability = float(model.predict_proba(features)[0][1])
    severity = int(probability >= THRESHOLD)

    logging.info(f"probability={probability:.4f}, severity={severity}")

    return {
        "severity_prediction": severity,
        "probability_severe": probability,
        "threshold": THRESHOLD
    }