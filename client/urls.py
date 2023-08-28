from django.urls import path
from . import views



urlpatterns = [
    path("dashboard/", views.dasboard, name="dash-board"),
    path("client-profile/", views.client_profile, name="client-profile"),
    path("transations/", views.transations, name="transations"),
]
