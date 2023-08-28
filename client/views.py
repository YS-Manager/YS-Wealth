from django.shortcuts import render



def dasboard(request):
    return render(request, "client/dashboard.html")


def client_profile(request):
    return render(request, "client/pages-profile.html")



def transations(request):
    return render(request, "client/transations.html")
