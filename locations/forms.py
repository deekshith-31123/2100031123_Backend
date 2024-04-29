# locations/forms.py
from django import forms
from .models import Country, Location

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_id', 'country_name', 'region_id']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['street_address', 'postal_code', 'city', 'state_province', 'country']
