# email_tracking_app/views.py
import requests
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import TrackedClick



def get_country_city_from_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        country = data.get('country', '')
        city = data.get('city', '')
        print(city)
    except Exception as e:
        # Handle API request errors
        country = ''
        city = ''
    
    return country, city

def track_click(request, click_id, offer_id, user_id):
    # Get user's IP address
    
    url = f"https://ipinfo.io/json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        ip_address = data.get('ip', '')
    except Exception as e:
        # Handle API request errors
        ip = ''

    
    

    # Use a service or library to get country and city based on IP
    country, city = get_country_city_from_ip(ip_address)

    # Save the tracked click information
    TrackedClick.objects.create(
        click_id=click_id,
        offer_id=offer_id,
        user_id=user_id,
        ip_address=ip_address,
        country=country,
        city=city,
    )

    # Redirect the user to the original destination
    # You might want to use a template or another method to create the destination URL.
    return redirect('https://www.example.com')

