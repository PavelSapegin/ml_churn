from typing import Dict, List, cast

import joblib
import pandas as pd
from fastapi import FastAPI

from preprocessing import create_new_features
from schemas import BatchRequest

app = FastAPI()

pipeline = joblib.load("model_pipeline.joblib")

@app.post("/predict")
def predict(request: BatchRequest) -> List[Dict[str, float]]:
    customers_dicts = [c.model_dump() for c in request.customers]
    df = pd.DataFrame(customers_dicts)
    ids = df["customer_id"]
    df = df.drop(columns="customer_id")
    preds = pipeline.predict_proba(df)[:,1]
    results = pd.DataFrame({"customer_id":ids,"prediction":preds})

    return cast(list[dict[str, float]],results.to_dict(orient="records"))
