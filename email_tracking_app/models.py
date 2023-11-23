# email_tracking_app/models.py
from django.db import models

class TrackedClick(models.Model):
    click_id = models.CharField(max_length=255)
    offer_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.click_id} - {self.user_id}'
