# djangoapp/views.py

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, logging
from .restapis import post_review, analyze_review_sentiments
from django.views.decorators.csrf import csrf_exempt


# lokalni moduli
from .populate import initiate
from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments  # 👈 dodan analyze_review_sentiments

logger = logging.getLogger(__name__)

# ... (login_user, logout_request, registration, get_cars, get_dealerships ostaju kako jesu) ...

def get_dealer_details(request, dealer_id):
    """
    Dohvati detalje o jednom dealeru prema ID-u.
    """
    if dealer_id:
        endpoint = "/fetchDealer/" + str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})

def get_dealer_reviews(request, dealer_id):
    """
    Dohvati sve reviewe za određenog dealera i dodaj sentiment za svaki review.
    """
    if dealer_id:
        endpoint = "/fetchReviews/dealer/" + str(dealer_id)
        reviews = get_request(endpoint)

        for review_detail in reviews:
            try:
                response = analyze_review_sentiments(review_detail.get("review", ""))
                print(response)
                review_detail["sentiment"] = response.get("sentiment", "neutral")
            except Exception as e:
                print(f"Sentiment analysis failed: {e}")
                review_detail["sentiment"] = "neutral"

        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})

