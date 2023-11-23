# email_tracking_app/urls.py
from django.urls import path
from .views import track_click

urlpatterns = [
    path('tr/<str:click_id>/<str:offer_id>/<str:user_id>/', track_click, name='tr'),
    
    # Add other URL patterns as needed
]
