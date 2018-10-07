from django.db import models


class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=False)