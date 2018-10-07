from django.db import models
from restaurant.models import Restaurant

STATUS_CHOICES = [
    (1, 'FREE'),
    (2, 'BUSY'),
    (3, 'CANCELED')
]


class Reservation(models.Model):
    reservation_id = models.IntegerField(primary_key=True)
    number_of_customers = models.IntegerField(null=False)
    reserved_date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    deposit = models.FloatField(null=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES)
    fee = models.FloatField()
