from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, logging

# import funkcije za popunjavanje baze
from .populate import initiate
# importaj modele
from .models import CarMake, CarModel

logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "status": "Invalid credentials"})


@csrf_exempt
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    firstName = data['firstName']
    lastName = data['lastName']
    email = data['email']

    try:
        User.objects.get(username=username)
        return JsonResponse({"userName": username, "error": "Already Registered"})
    except User.DoesNotExist:
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=firstName,
            last_name=lastName,
            email=email,
        )
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})


# --- New view to get cars ---
def get_cars(request):
    # ako nema niti jednog CarModel zapisa, pokreni seed
    if CarModel.objects.count() == 0:
        initiate()

    car_models = CarModel.objects.select_related("car_make")
    cars = []
    for cm in car_models:
        cars.append({"CarModel": cm.name, "CarMake": cm.car_make.name})
    return JsonResponse({"CarModels": cars})

