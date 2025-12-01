from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json, os

# Path to JSON file
DATA_FILE = "app\static\data.json"

def read_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------------- PAGES --------------------------
def home(request):
    return render(request, "home.html")

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def dashboard(request):
    return render(request, "dashboard.html")

# ---------------------- API --------------------------
@api_view(["POST"])
def register_api(request):
    data = request.data
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")

    users = read_data()

    # check existing user
    for u in users["users"]:
        if u["email"] == email:
            return Response({"status": "error", "message": "User already exists"})

    # add new user
    new_user = {
        "email": email,
        "password": password,
        "name": name
    }

    users["users"].append(new_user)
    write_data(users)

    return Response({"status": "success", "message": "Registered Successfully"})


@api_view(["POST"])
def login_api(request):
    data = request.data
    email = data.get("email")
    password = data.get("password")

    users = read_data()

    # validate user
    for u in users["users"]:
        if u["email"] == email and u["password"] == password:
            return Response({
                "status": "success",
                "message": "Login success",
                "user": u
            })

    return Response({"status": "error", "message": "Invalid Email or Password"})
