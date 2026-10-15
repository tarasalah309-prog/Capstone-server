from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DeviceMessage(BaseModel):
    event: str

@app.get("/")
def home():
    return {"status": "server is running"}

@app.post("/predict")
def predict(message: DeviceMessage):
    # Temporary response for testing connectivity
    return {
        "label": "connected" if message.event == "test"
                 else "unknown",
        "confidence": 1.0
    }