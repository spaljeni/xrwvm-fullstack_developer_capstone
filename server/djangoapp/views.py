# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# =========================
# AUTH VIEWS
# =========================

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    resp = {"userName": username}
    if user is not None:
        login(request, user)
        resp["status"] = "Authenticated"
    return JsonResponse(resp)

def logout_user(request):
    logout(request)  # Terminate user session
    data = {"userName": ""}  # Return empty username
    return JsonResponse(data)

@csrf_exempt
def registration(request):
    # Load JSON data from the request body
    data = json.loads(request.body)
    username   = data['userName']
    password   = data['password']
    first_name = data['firstName']
    last_name  = data['lastName']
    email      = data['email']

    username_exist = False
    try:
        User.objects.get(username=username)
        username_exist = True
    except Exception:
        logger.debug("%s is new user", username)

    if not username_exist:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "error": "Already Registered"})

# =========================
# DEALERS API (demo JSON)
# =========================

def get_dealerships(request):
    """Simple JSON demo; kasnije zamijeni stvarnim izvorom (DB/API)."""
    dealers = [
        {"id": 1, "name": "Best Cars Chicago", "city": "Chicago, IL", "phone": "(312) 555-0101"},
        {"id": 2, "name": "Lakeview Motors",   "city": "Evanston, IL", "phone": "(847) 555-0102"},
        {"id": 3, "name": "South Loop Auto",   "city": "Chicago, IL", "phone": "(312) 555-0103"},
    ]
    return JsonResponse({"dealers": dealers})
