from django.urls import path
from . import views


urlpatterns = [
    path("log-in/", views.login, name="log-in"),
    path("sign-up/", views.signup, name="sign-up"),
]
