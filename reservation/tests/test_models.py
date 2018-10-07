from datetime import datetime

from django.test import TestCase
from model_mommy import mommy
from reservation.models import Reservation


class ReservationTestCase(TestCase):

    def setUp(self):
        self.mocked_class = mommy.make_recipe('reservation.tests.recipes.reservation')

    def test_get_reservation(self):
        reservation = Reservation.objects.get(pk=self.mocked_class.reservation_id)
        assert reservation is not None

    def test_update_get_reservation_by_reserved_date(self):
        obj = Reservation.objects.filter(reserved_date=datetime.now())
        assert obj is not None

    def test_list_reservation(self):
        reservations = list(Reservation.objects.all())
        assert len(reservations) >= 1
