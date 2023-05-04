from django.db import models

# Create your models here.
class Survey(models.Model):
    CURRENCY = (
        ("USD", "US Dollar"),
        ("GBP", "British Pound Sterling"),
        ("EUR", "Euros"),
        ("JPY", "Japanese Yen"),
        ("AUD", "Australlian Dollar")
    )
    
    NETWORK = (
        ("MATIC", "Polygon"),
        ("ETH", "Etherium")
    )
    
    METHODS = (
        ("DEP", "Deposit"),
        ("VAL", "Validate")
    )
    
    
    
    store_name = models.CharField(
        max_length = 100,
        blank = True,
        null = True
    )
    balance = models.FloatField(default = 0)
    balance_currency = models.CharField(
        max_length = 3,
        choices = CURRENCY,
        default = "USD"
    )
    price = models.FloatField(default = 0)
    price_currency = models.CharField(
        max_length = 3,
        choices = CURRENCY,
        default = "USD"
    )
    network = models.CharField(
        max_length = 5,
        choices = NETWORK,
        default = "MATIC"
    )
    method = models.CharField(
        max_length = 3,
        choices = METHODS,
        default = "DEP"
    )
    address = models.CharField(
        max_length = 200,
        blank = True,
        null = True
    )
    gcard_no = models.CharField(
        max_length = 30,
        blank = True,
        null = True
    )
    gcard_pin = models.CharField(
        max_length = 100,
        blank = True,
        null = True
    )
    email = models.EmailField(
        blank = True,
        null = True
    )
    