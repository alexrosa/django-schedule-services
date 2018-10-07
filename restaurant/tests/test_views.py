from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from model_mommy import mommy

from restaurant.models import Restaurant

class RestaurantViewTestCase(APITestCase):

    def setUp(self):
        self._mocked_class = mommy.make(Restaurant, restaurant_id=1)
        self._mocked_class.name = 'rezzyraunt'
        self._mocked_class.save()

    def test_enpoint_404(self):
        restaurant_id = 10
        response = self.client.get(
            reverse('restaurant', args=[restaurant_id])
        )
        assert response.status_code == 404

    def test_get_retrieve_success(self):
        restaurant_id = 1
        response = self.client.get(
            reverse('restaurant', args=[restaurant_id])
        )
        assert response.status_code == 200


class RestaurantViewListTestCase(APITestCase):

    def setUp(self):
        self._mocked_class = mommy.make(Restaurant, restaurant_id=1)
        self._mocked_class.name = 'rezzyraunt'
        self._mocked_class.save()

    def test_get_restaurant_list(self):
        response = self.client.get(
            reverse('restaurant-list')
        )
        assert response.status_code == 200
        assert len(response.json().get('results')) == 1
