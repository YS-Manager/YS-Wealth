from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import ClientProfile, ClientInvestment, Stock, CLientTransations

from twilio.rest import Client

import random

from .forms import ClientProfileForm, UserForm, OPTForm

from .utils import send_sms, graph



@login_required(login_url="log-in")
def dasboard(request):
    investment = ClientInvestment.objects.get(user=request.user)
    stocks = Stock.objects.filter(user=request.user)
    return render(request, "client/dashboard.html", {
        "investment": investment,
        "stocks": stocks,
        "chart": graph(request),
    })


@login_required(login_url="log-in")
def client_profile(request):
    client = get_object_or_404(ClientProfile, user=request.user)
    
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        client_form = ClientProfileForm(request.POST, request.FILES, instance=client)
        if user_form.is_valid() and client_form.is_valid():
            user_form.save()
            client_form.save()
            return redirect("client-profile")
    
    user_form = UserForm(instance=request.user)
    client_form = ClientProfileForm(instance=client)
    return render(request, "client/user-profile.html", {
        "user": user_form,
        "profile": client_form,
        "client": client,
    })



@login_required(login_url="transations")
def transations(request):
    transations = CLientTransations.objects.filter(user=request.user)
    return render(request, "client/transations.html", {
        "transations": transations,
    })


@login_required(login_url="log-in")
def withdraw_amount(request):
    client_info = ClientProfile.objects.get(user=request.user)
    if request.method == "POST":
        account_sid = 'AC4df7ec37cccef22b3dc88d06496973ea'
        auth_token = '7052666be54946f1d2cb663bb6813919'
        client = Client(account_sid, auth_token)
        data = request.POST
        username=request.user.username
        contact=client_info.phone_number
        amount=data["amount"]
        user_data = [
            {"name": username, "phone": contact, "amount": amount},
            {"name": "Manoj", "phone": "7838367854", "amount": f"{username} want to withdraw {amount} rupees."},
        ]
        for user in user_data:
            otp = random.randint(100000, 999999)
            request.session[user["name"]] = otp
            message = client.messages.create(
                from_= "+13253996109",
                body=f'YS-WEALTH\nusername: {user.get("name")}\namount: {user.get("amount")}\nYour OTP is {otp}',
                to=f"+91{user['phone']}"
            )
        return redirect("otp-page")
    return render(request, "client/withdraw.html")


@login_required(login_url="log-in")
def otp_page(request):
    otpform = OPTForm()
    if request.method == "POST":
        form = OPTForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data["otp1"] == str(request.session[request.user.username]) and data["otp2"] == str(request.session["Manoj"]):
                return redirect("otp-success")
            send_sms(request)
            return render(request, "client/otp.html", {
                "otpform": otpform,
            })
    return render(request, "client/otp.html", {
        "otpform": otpform,
    })


@login_required(login_url="log-in")
def otp_success(request):
    return render(request, "client/otp-success.html")