from django.shortcuts import render, redirect
from .forms import CountryForm, LocationForm
from .models import Location, Country
from django.db.models import Value
#adding data trough frontend
def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_location')  # Redirects to the location form after saving
    else:
        form = CountryForm()
    return render(request, 'add_country.html', {'form': form})

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_location_success')
    else:
        form = LocationForm()
    return render(request, 'add_location.html', {'form': form})

def add_location_success(request):
    return render(request, 'add_location_success.html')


#using join and no join
def get_canadian_addresses():
    return Location.objects.filter(country__country_name='Canada').values(
        'location_id', 'street_address', 'postal_code', 'city', 'state_province', 'country__country_id'
    )

def get_canadian_country_details():
    canadian_details = Country.objects.filter(country_name='Canada').values(
        'country_id', 'country_name', 'region_id'
    )
    return canadian_details


def display_addresses(request):
    addresses_with_join = get_canadian_addresses()
    addresses_no_join = get_canadian_country_details()
    return render(request, 'display_addresses.html', {
        'addresses_with_join': addresses_with_join,
        'addresses_no_join': addresses_no_join
    })

#view all
def view_all_locations():
    return Location.objects.all()

def view_all_countries():
    return Country.objects.all()

def display_all(request):
    locations = view_all_locations()
    countries = view_all_countries()
    return render(request, 'displayall.html', {  # Ensure this matches your HTML file name
        'locations': locations,
        'countries': countries
    })

def homepage(request):
    return render(request,"home.html")


