from django.urls import path
from . import views



urlpatterns = [
    path("dashboard/", views.dasboard, name="dash-board"),
    path("client-profile/", views.client_profile, name="client-profile"),
    path("transations/", views.transations, name="transations"),
    path("withdraw/", views.withdraw_amount, name="withdraw"),
    path("otp/", views.otp_page, name="otp-page"),
    path("otp-success/", views.otp_success, name="otp-success"),
]
