# locations/urls.py
from django.urls import path
from .views import add_country, add_location, add_location_success, display_addresses,  display_all,homepage

urlpatterns = [
    #to insert through frontend
    path('add-country/', add_country, name='add_country'),
    path('add-location/', add_location, name='add_location'),
    path('success/', add_location_success, name='add_location_success'),
    #using join and no join
    path('display-addresses/', display_addresses, name='display_addresses'),

    #select all
    path('display_all/', display_all, name='display_all'),

    path("",homepage,name="home"),

]
