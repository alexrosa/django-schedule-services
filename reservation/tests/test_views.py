from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from model_mommy import mommy


class ReservationViewTestCase(APITestCase):

    def setUp(self):
        self.mocked_class = mommy.make_recipe('reservation.tests.recipes.reservation')

    def test_404_endpoint(self):
        restaurant_id = 0
        reservation_id = 0
        response = self.client.get(
            reverse('reservation', args=[restaurant_id, reservation_id])
        )
        assert response.status_code == 404

    def test_get_reservation(self):
        response = self.client.get(
            reverse('reservation', args=[self.mocked_class.restaurant.restaurant_id,
                                         self.mocked_class.reservation_id])
        )
        assert response.status_code == 200

    def test_get_list_reservation(self):
        response = self.client.get(
            reverse('reservation-list', args=[self.mocked_class.restaurant.restaurant_id])
        )
        assert response.status_code == 200
        assert len(response.json().get('results')) == 1
