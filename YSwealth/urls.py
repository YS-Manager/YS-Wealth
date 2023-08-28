from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("wealth.urls")),
    path("account/", include("account.urls")),
    path("client/", include("client.urls")),
]
