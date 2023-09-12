from django.contrib import admin

from .models import ClientProfile, ClientInvestment, StockSector, Stock, CLientTransations


admin.site.register(ClientProfile)
admin.site.register(ClientInvestment)
admin.site.register(CLientTransations)
admin.site.register(StockSector)

admin.site.register(Stock)