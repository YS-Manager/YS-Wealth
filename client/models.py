from django.db import models
from django.contrib.auth.models import User



class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.ImageField(upload_to="client/images", blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    client_code = models.CharField(unique=True, max_length=20)

    class Meta:
        verbose_name_plural = "Client Profile"

    def __str__(self):
        return self.user.username


class ClientInvestment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="investment")
    invest_amount = models.CharField(max_length=20)
    current_value = models.CharField(max_length=20)
    returns = models.CharField(max_length=20)
    profit_loss = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural= "Client Investment"

    def __str__(self):
        return self.user.username
    

class StockSector(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Stock Sector"

    def __str__(self):
        return self.name


class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stock_info")
    sector = models.ForeignKey(StockSector, on_delete=models.CASCADE, related_name="stocks")
    stock_name = models.CharField(max_length=50, unique=True)
    dp = models.CharField(max_length=20)
    total_stock = models.CharField(max_length=20)
    close_rate = models.CharField(max_length=20)
    dp_value = models.CharField(max_length=20)
    collateral_value = models.CharField(max_length=20)

    def __str__(self):
        return self.stock_name
    


class CLientTransations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    trans_amount = models.CharField(max_length=10000000)

    class Meta:
        verbose_name_plural = "Client Transations"

    def __str__(self) -> str:
        return self.user.username
