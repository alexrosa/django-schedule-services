from django.test import TestCase

from restaurant.models import Restaurant


class RestaurantTestCase(TestCase):

    def setUp(self):
        Restaurant.objects.create(name="rezzyraunt")

    def test_get_restaurant(self):
        restaurant = Restaurant.objects.get(pk=1)
        assert restaurant.pk == 1

    def test_delete_restaurant(self):
        restaurant = Restaurant.objects.get(pk=1)
        Restaurant.delete(restaurant)
        assert True

