from django.shortcuts import render, redirect
from .forms import SignupForm
# from .models import User
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth






def signup(request):
    signup_form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            print(password)
            user.set_password(password)
            user.save()
            return redirect("log-in")
        return render(request, "account/sign-up.html", {
            "form": form,
        })

    return render(request, "account/sign-up.html", {
        "form": signup_form
    })


def log_in(request):
    if request.user.is_authenticated:
        return redirect("dash-board")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("dash-board")
        else:
            return redirect("log-in")
    return render(request, "account/login.html")


@login_required(login_url="log-in")
def log_out(request):
    logout(request)
    return redirect("log-in")
