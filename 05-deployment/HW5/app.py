from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load the pipeline
with open('pipeline_v2.bin', 'rb') as f:
    pipeline = pickle.load(f)

class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.post("/predict")
def predict(client: Client):
    data = [client.dict()]
    prob = pipeline.predict_proba(data)[0][1]
    return {"probability": prob}
