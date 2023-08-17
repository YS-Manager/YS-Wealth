from django.shortcuts import render



def home(request):
    return render(request, "wealth/home.html")


def about(request):
    return render(request, "wealth/about.html")


def service(request):
    return render(request, "wealth/service.html")


def contact(request):
    return render(request, "wealth/contact.html")


def features(request):
    return render(request, "wealth/feature.html")


def team(request):
    return render(request, "wealth/team.html")


def testimonial(request):
    return render(request, "wealth/testimonial.html")