# Uncomment the required imports before adding the code

import json
import logging
from datetime import datetime

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt

from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    """
    Backend login endpoint:
      - GET: return info message (ne parsira JSON)
      - POST: očekuje JSON body: {"userName": "...", "password": "..."}
              autentificira i vraća status
    """
    if request.method != "POST":
        return JsonResponse(
            {"detail": "Login endpoint. Send POST with JSON {userName, password}."},
            status=200,
        )

    # POST
    try:
        body = request.body.decode("utf-8") if request.body else "{}"
        data = json.loads(body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("userName") or data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"error": "userName and password required"}, status=400)

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"}, status=200)

    return JsonResponse({"userName": username, "status": "Invalid credentials"}, status=401)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
#     ...

# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
#     ...

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
#     ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
#     ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
#     ...

# Create a `add_review` view to submit a review
# def add_review(request):
#     ...
