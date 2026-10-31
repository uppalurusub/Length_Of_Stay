import requests
API_URL="http://localhost:8000/los/predict"
def predict(payload:dict):
    r=requests.post(API_URL,json=payload,timeout=30)
    r.raise_for_status()
    return r.json()
