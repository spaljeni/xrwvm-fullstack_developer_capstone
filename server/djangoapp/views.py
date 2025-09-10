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

@csrf_exempt
def login_user(request):
    """
    Backend login endpoint:
      - GET: info message (ne parsira JSON)
      - POST: JSON body: {"userName": "...", "password": "..."}
    """
    if request.method != "POST":
        return JsonResponse(
            {"detail": "Login endpoint. Send POST with JSON {userName, password}."},
            status=200,
        )

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


@csrf_exempt
def logout_user(request):
    """
    GET /djangoapp/logout -> terminates session and returns {"userName": ""}
    """
    if request.method != "GET":
        return JsonResponse({"error": "GET only"}, status=405)

    logout(request)  # Terminate user session
    data = {"userName": ""}  # Return empty username
    return JsonResponse(data, status=200)


# NEW: registration endpoint
@csrf_exempt
def registration(request):
    """
    POST /djangoapp/register
      Body JSON:
        {
          "userName": "...",
          "password": "...",
          "firstName": "...",
          "lastName": "...",
          "email": "..."
        }
      Creates user, logs in, returns {"userName": "...", "status": "Authenticated"}
      If username exists -> {"userName": "...", "error": "Already Registered"}
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("userName")
    password = data.get("password")
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")

    if not all([username, password, first_name, last_name, email]):
        return JsonResponse({"error": "Missing required fields"}, status=400)

    # Check if user exists
    try:
        User.objects.get(username=username)
        # already registered
        return JsonResponse({"userName": username, "error": "Already Registered"}, status=200)
    except User.DoesNotExist:
        logger.debug("%s is new user", username)

    # Create and log in
    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password,
        email=email,
    )
    login(request, user)
    return JsonResponse({"userName": username, "status": "Authenticated"}, status=200)

# (stubs you may fill later)
# def get_dealerships(request): ...
# def get_dealer_reviews(request, dealer_id): ...
# def get_dealer_details(request, dealer_id): ...
# def add_review(request): ...
