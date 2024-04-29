from django.db import models

# Create your models here.

# locations/models.py
from django.db import models

class Country(models.Model):
    country_id = models.CharField(max_length=2, primary_key=True)
    country_name = models.CharField(max_length=50)
    region_id = models.IntegerField()

    def __str__(self):
        return self.country_name

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=125)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street_address}, {self.city}"
