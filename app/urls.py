from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),

    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("dashboard/", dashboard, name="dashboard"),

    # API
    path("api/register/", register_api),
    path("api/login/", login_api),
]
