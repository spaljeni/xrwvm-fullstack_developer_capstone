# djangoapp/restapis.py

import os
import requests
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

# .env primjer:
# backend_url=http://localhost:3030
# sentiment_analyzer_url=https://<your-code-engine-url>/
backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url",
    default="http://localhost:5050/"
)

def get_request(endpoint, **kwargs):
    """
    Generic GET helper for backend services.
    Usage: get_request("/fetchDealers"), get_request("/fetchReviews", dealerId="15")
    """
    request_url = backend_url + endpoint
    try:
        response = requests.get(request_url, params=kwargs)  # params sigurno enkodira
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return {"error": "Network exception occurred"}

def analyze_review_sentiments(text: str):
    """
    Call the sentiment analyzer microservice.
    """
    encoded_text = quote_plus(text)  # npr. "Fantastic services" -> "Fantastic+services"
    request_url = sentiment_analyzer_url + "analyze/" + encoded_text
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"error": "Sentiment analysis failed"}

def post_review(data_dict: dict):
    """
    Post a review to the backend.
    Očekuje dict sa svim potrebnim poljima (dealerId, name, review, purchase, itd.)
    """
    request_url = backend_url + "/insert_review"
    print(f"POST to {request_url} with payload: {data_dict}")
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return {"error": "Network exception occurred"}
